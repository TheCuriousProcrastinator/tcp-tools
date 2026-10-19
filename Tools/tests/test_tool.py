import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

MOD = Path(__file__).resolve().parents[1] / 'vibe_handoff.py'
spec = importlib.util.spec_from_file_location('vh', MOD)
vh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vh)

class ToolTests(unittest.TestCase):
    def test_version_parser_and_idempotence(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            def git(*args):
                return subprocess.check_output(['git',*args], cwd=root, text=True).strip()
            git('init','-q')
            git('checkout','-qb','main')
            git('config','user.email','test@example.com')
            git('config','user.name','Test')
            git('remote','add','origin','git@github.com:TheCuriousProcrastinator/Fixture.git')
            (root/'VIBECODING_HANDOFF.md').write_text('# Context\n\nThe old history stays.\n')
            (root/'chrome-extension').mkdir()
            (root/'chrome-extension/manifest.json').write_text('{"manifest_version":3,"version":"0.2.1"}')
            git('add','-A')
            git('commit','-qm','fixture')
            msg=vh.run(root,'update',True)
            self.assertIn('UPDATED:', msg)
            text=(root/'VIBECODING_HANDOFF.md').read_text()
            self.assertIn('version `0.2.1`',text)
            self.assertIn('The old history stays.',text)
            self.assertIn('PASS',vh.run(root,'check',True))
            # Local staged version change requires refresh, check fails until update.
            (root/'chrome-extension/manifest.json').write_text('{"manifest_version":3,"version":"0.2.2"}')
            git('add','chrome-extension/manifest.json')
            with self.assertRaisesRegex(RuntimeError,'stale'):
                vh.run(root,'check',True)
            # To regenerate, first commit the standalone test handoff in this disposable fixture.
            git('add','VIBECODING_HANDOFF.md')
            git('commit','-qm','initial handoff')
            # Still staged source? committed along with previous fixture commit.
            self.assertIn('version `0.2.2`', vh.block('Fixture','main',vh.source_metadata(root,vh.index_paths(root)),'x'))
            vh.run(root,'update',True)
            self.assertIn('PASS', vh.run(root,'check',True))

    def test_marker_safety(self):
        with self.assertRaisesRegex(RuntimeError, 'Ambiguous'):
            vh.replace_section(vh.START+'\n'+vh.START+'\n'+vh.END,'X')
        self.assertEqual(vh.replace_section('intro', 'X'), 'X\n\nintro')

if __name__ == '__main__':
    unittest.main()

class SourceVersionTests(unittest.TestCase):
    def test_xcodegen_xcode_and_sparkle(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            def git(*args):
                return subprocess.check_output(['git',*args],cwd=root,text=True).strip()
            git('init','-q')
            git('config','user.email','test@example.com')
            git('config','user.name','Test')
            (root/'project.yml').write_text('MARKETING_VERSION: "1.0.26"\nCURRENT_PROJECT_VERSION: "40"\n')
            (root/'appcast.xml').write_text('''<rss xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle"><channel><item><sparkle:version>449</sparkle:version><sparkle:shortVersionString>1.3.11</sparkle:shortVersionString></item></channel></rss>''')
            git('add','project.yml','appcast.xml')
            data=vh.source_metadata(root,vh.index_paths(root))
            self.assertIn(('project.yml','1.0.26','40'),data)
            self.assertIn(('appcast.xml','1.3.11','449'),data)
