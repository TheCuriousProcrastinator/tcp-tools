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

The first rollout prepared generated handoff facts only. The second rollout
installs local commit hooks and integrates the known Sparkle release scripts.
Human feature decisions, tests, and external publication remain separately verified.

## Workflow after full rollout

1. Develop and **validate exact source files in the real Mac checkout**.
2. Stage tested source; maintain the handoff's narrative for the change.
3. Run `update`, stage the handoff, run `check`, inspect diff, commit/push.
4. After publication, verify release and update feed, refresh handoffs in the
   source and updates repos with documentation-only commits.
5. The opt-in per-checkout commit hook now updates the generated facts
   automatically, but never substitutes for testing or manual development notes.

Other instructions in each repository retain precedence for project-specific
build commands, manual validation, and release signing.


## Local commit/release integration (2026-10-19)

Each Vibe Coding repository now tracks `Tools/vibe_handoff.py`,
`.githooks/pre-commit` and `.githooks/install.sh`. Run the installer
once in each clean checkout to activate the local pre-commit hook.
The hook synchronizes only the generated handoff section with staged
source metadata and the authenticated GitHub release API. It refuses
unstaged handoff edits and unverified remote release status. It does
not verify builds or replace human-maintained feature/bug context.

Existing Sparkle release scripts for Draftava, Doit Then and ToMP4
are integrated for update-repo and post-publication source handoffs.
For other projects, release publication still requires manually
verifying the external channel and then committing the updated handoff.
No GitHub Actions are run automatically.
