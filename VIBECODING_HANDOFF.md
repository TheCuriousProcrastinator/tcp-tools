# TCP Tools - Development Handoff

**Updated:** 2026-10-02

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
