import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
HOOK = PKG / 'hook/pre-commit'
if not HOOK.exists():
    HOOK = PKG.parent / '.githooks/pre-commit'


class HookIntegrationTests(unittest.TestCase):
    def test_commit_sync_and_unstaged_safety(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'repo'
            root.mkdir()
            def git(*args, check=True):
                return subprocess.run(['git', *args], cwd=root, text=True,
                                      capture_output=True, check=check)
            git('init', '-q')
            git('checkout', '-qb', 'main')
            git('config', 'user.email', 'test@example.com')
            git('config', 'user.name', 'Test')
            git('remote', 'add', 'origin', 'git@github.com:TheCuriousProcrastinator/Fixture.git')
            (root / 'VIBECODING_HANDOFF.md').write_text('# Fixture handoff\n\nManual context.\n')
            (root / 'manifest.json').write_text('{"version":"1.0.0"}\n')
            git('add', '-A')
            git('commit', '-qm', 'initial')
            (root / 'Tools').mkdir()
            (root / '.githooks').mkdir()
            shutil.copy2(PKG / 'vibe_handoff.py', root / 'Tools' / 'vibe_handoff.py')
            shutil.copy2(HOOK, root / '.githooks/pre-commit')
            git('config', 'core.hooksPath', '.githooks')
            bin_dir = Path(tmp) / 'bin'
            bin_dir.mkdir()
            gh = bin_dir / 'gh'
            gh.write_text('#!/bin/sh\nprintf \'%s\\n\' \'{"tag_name":"v1.0.0","draft":false,"prerelease":false}\'\n')
            gh.chmod(0o755)
            env = os.environ.copy()
            env['PATH'] = str(bin_dir) + os.pathsep + env['PATH']
            # Hook must refresh the staged handoff, not just the working file.
            (root / 'manifest.json').write_text('{"version":"1.0.1"}\n')
            git('add', 'manifest.json')
            result = subprocess.run(['git', 'commit', '-qm', 'version bump'],
                                    cwd=root, text=True, capture_output=True, env=env)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            staged_handoff = git('show', 'HEAD:VIBECODING_HANDOFF.md').stdout
            self.assertIn('version `1.0.1`', staged_handoff)
            self.assertIn('Manual context.', staged_handoff)
            self.assertIn('Published GitHub release `v1.0.0`', staged_handoff)
            # An unstaged manual handoff edit must never be silently overwritten.
            with (root / 'VIBECODING_HANDOFF.md').open('a') as f:
                f.write('\nImportant human edit.\n')
            (root / 'manifest.json').write_text('{"version":"1.0.2"}\n')
            git('add', 'manifest.json')
            rejected = subprocess.run(['git', 'commit', '-qm', 'should refuse'],
                                      cwd=root, text=True, capture_output=True, env=env)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn('unstaged changes', rejected.stderr + rejected.stdout)
            self.assertIn('Important human edit.', (root / 'VIBECODING_HANDOFF.md').read_text())
            self.assertIn('1.0.1', git('show', 'HEAD:manifest.json').stdout)


if __name__ == '__main__':
    unittest.main()
