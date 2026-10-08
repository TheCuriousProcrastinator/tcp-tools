# TCP Tools - Development Handoff

**Updated:** 2026-10-02

## Shared Vibe Coding workflow rules (2026-10-08)

### Documentation-only handoff exception
- When the user explicitly requests a documentation-only update, ChatGPT may edit the existing root `VIBECODING_HANDOFF.md` directly through GitHub without requiring a Mac build or a local checkout step.
- First inspect the actual repository, target branch, and existing handoff. Change only the handoff, preserve historical project context, and verify the resulting GitHub file and commit. Do not use this exception for application code, tests, scripts, configuration, workflows, version/build changes, release assets, or other build-affecting files.
- Before the next local development change, fetch the remote branch and reconcile the updated handoff with the local checkout. Never overwrite or silently reset unrelated local changes.
- The normal rule remains: validate the exact executable/build-affecting changes in the real Mac checkout before committing or pushing those changes. Include a current handoff with every meaningful validated development commit.

### Temporary worktrees, releases, and logs
- Create temporary Git worktrees under `/Users/alex/Desktop/tmp/<project>-...` using a project-specific name.
- Put release working folders, temporary release artifacts, staging directories, and build/release logs under `/Users/alex/Desktop/tmp/<project>-release-...`.
- Do not create disposable worktrees inside `/Users/alex/Documents/Vibe Coding`.
- Do not place release artifacts or logs directly on the Desktop root.
- After a successful verified release, remove temporary worktrees and temporary release artifacts when safe. Do not remove active worktrees, uncommitted work, published assets, or permanent project files.
- Retain failure logs only when useful for debugging; remove unnecessary temporary logs.
- These instructions govern future operations and take precedence over historical temporary-path examples elsewhere in this handoff.

### Low-overhead development defaults
- Use ChatGPT plus GitHub inspection and Mac-local Terminal scripts by default; do not use Codex, ChatGPT Work, separately billed API agents, or GitHub Actions runners unless explicitly requested.
- Prefer existing project scripts. Give one local command block to apply, build, test, and launch an executable change, then a separate commit/push block only after required validation is confirmed.
- Documentation-only updates under the exception above do not require a rebuild.

## Project

TCP Tools is the static landing page for downloadable tools from The Curious Procrastinator.

## Repository

- GitHub: `TheCuriousProcrastinator/tcp-tools`
- Default branch: `main`
- Source baseline before this policy migration: `4531edc5a61cac09d6a6e296852bfbeafce4965b`
- Deployment configuration: `netlify.toml`
- Requested Netlify site: `tcp.netlify.app`

Always verify the current repository HEAD before making changes.

## Architecture

The site is static.

Relevant files:

- `index.html`
- `styles.css`
- `script.js`
- `netlify.toml`
- `assets/tool-library-hero.png`

Local preview can use:

`python3 -m http.server 8888`

## GitHub Actions policy

Normal development and deployment validation is authoritative only when performed locally.

The repository contains `.github/workflows/manual-validation.yml`.

It is intentionally manual-only through `workflow_dispatch`.

GitHub Actions must not run automatically for pushes, pull requests, tags, schedules, or other repository events.

Actions may run only when the user explicitly requests optional clean-environment verification.

Development and publication do not depend on GitHub Actions.

## Netlify

This repository is configured as a static Netlify site.

This migration does not change `netlify.toml`, site content, deployment configuration, or Netlify behavior.

GitHub Actions policy and Netlify deployment behavior are separate concerns.

## Development workflow

Before modifying the project:

1. `git fetch origin`
2. verify repository, branch, and expected HEAD
3. inspect `git status --short`
4. stop rather than overwrite, reset, stash, or merge unrelated work
5. make the smallest reliable change
6. preview and validate locally
7. manually verify visual changes when required
8. commit and push only the exact locally validated files
9. update this handoff with every meaningful development commit

GitHub remains read-only until required local validation succeeds.

## Policy migration scope

This migration changes only:

- `.github/workflows/manual-validation.yml`
- `VIBECODING_HANDOFF.md`

It does not change site content, JavaScript, styling, assets, Netlify configuration, or deployment behavior.

## Next development task

Verify this handoff and the current repository before selecting the next site change.
