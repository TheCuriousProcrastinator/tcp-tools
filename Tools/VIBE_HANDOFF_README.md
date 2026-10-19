# Vibe Handoff (local-validation pilot)

Covers 19 GitHub repositories owned by TheCuriousProcrastinator, including all apps,
web projects, extensions and update feeds visible on 2026-10-18.

`vibe_handoff.py update CHECKOUT` inserts/replaces a bounded generated section at
the start of VIBECODING_HANDOFF.md. It reads VERSION data from **Git's index**,
and stable GitHub Releases via authenticated `gh api`. Any other storefront,
Cloudflare, notarization, manual QA and actual app behavior are explicitly
**unverified**. It does not guess or modify the historical narrative.

`vibe_handoff.py check CHECKOUT` checks the generated text against staged/indexed
metadata and GitHub release data. It fails if stale. It never commits, pushes,
tags, creates/releases assets, triggers Actions, touches application code or
installs Git hooks.

This first rollout only prepares local copies of updated handoffs and tests the
tool on the user's Mac. Release-script wiring and hook installation are a
separate validated step. It is not yet an unattended end-to-end solution.

## Workflow after full rollout

1. Develop and **validate exact source files in the real Mac checkout**.
2. Stage tested source; maintain the handoff's narrative for the change.
3. Run `update`, stage the handoff, run `check`, inspect diff, commit/push.
4. After publication, verify release and update feed, refresh handoffs in the
   source and updates repos with documentation-only commits.
5. Future optional commit hooks can run `check` as a safety net; don't overwrite
   existing hooks or assume this substitutes for testing.

Other instructions in each repository retain precedence for project-specific
build commands, manual validation, and release signing.
