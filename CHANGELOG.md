# Changelog

All notable changes to the **Erase on Demand** dataset, codebooks, and repository documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Site
- Page title set to the study title; links to methodology, codebook and repository now point to `Provereno-Media/Erase-On-Demand-Bad-Actors-VS-Journalists`.
- Funding block added above the footer: logos of the EU (co-funding), EFCSN and Provereno, in that order. Logo files are in `site/assets/`.
- "About this research": funding programme renamed to the EU Citizens, Equality, Rights and Values (CERV) programme (via EFCSN, https://efcsn.com/cerv-2026/), replacing "Tech Accountability Grants"; the EACEA disclaimer (as in `README.md`) moved into this block.
- "Narrative report" note added to "About the data"; the link will be added on publication.
- Case details: duplicate "DSA articles coded" line removed; `failed_control` values separated with ", ".

### Repository
- 1.0.0 marked as released (the "planned" label removed). Git tags `v1.0.0`–`v1.0.4` mark the repository state of each data release.
- Planned: the GitHub Release and Zenodo DOI will be made once the full-text Russian and English reports are added to the repository.
- README, LICENSE, SECURITY: funding programme named as CERV (via EFCSN) instead of "Tech Accountability Grants".
- Removed `data/Gaylan/` (byte-identical duplicate of `data/case-notes/Gaylan/`, which SRC-035 links to).
- Removed `data/Aiplex/`: a saved Google Transparency Report page whose data tables load by script, so the copy held no AiPlex figures; it also bundled Google's analytics.js. The AiPlex figures are cited from the live report.
- Renamed `data/case-notes/shishkin-like/shisnkin_like_*.jpg` to `shishkin_like_*.jpg`.
- Removed `docs/roadmap-v1.0.md` (internal Russian-language plan for the 1.0.0 release, now complete; kept in git history).

---

## [1.0.4] - 2026-11-18

### Added
- `cases.csv`: new field `failure_points` (`FP1`–`FP6`), using the numbering of the six failure points in Part 2 of the report. Values are derived from existing fields by the rules in `codebook.md` §1.2.10; `failed_control` is unchanged.
- `codebook.md` §1.2.10: failure point definitions, assignment rules, DSA article mapping and a correspondence table between `failed_control` and the failure points.
- `validate.py` checks `failure_points` values; the site shows failure points and DSA articles in case details.

### Changed
- `dsa_articles_implicated` recoded for all episodes from the failure point mapping (previously `17,20,34,35` for 32 of 33 episodes). Article 23 now appears in 6 episodes and Article 22 in 5.

---

## [1.0.3] - 2026-11-18

### Changed
- `claimant_identity_verified` set to `no` for `RESP-004`, `RESP-005`, `LMC-002`, `LMC-003`, `GAYLAN-001` and `SHISH-002`: a claimant named in a notice is not an independently verified identity (see Known Limitations).
- `ELIM-001`: `SRC-004` removed (it does not cover this case); supported by `SRC-005`.
- `ELIM-003`: `SRC-004` replaced with `SRC-005`; `target_country` corrected from `ES` to `MX`. `ACT-022` (Página 66) corrected to `MX`, Mexican local outlet (Campeche).
- `ELIM-005`, `ELIM-006`: `SRC-004` and `SRC-007` (neither covers these cases) replaced with Qurium, "Dark Ops Undercovered: Episode I" (`SRC-055`); `ELIM-006` also cites The Elephant's own account (`SRC-056`); `date_start` set to 2020-11.
- `SRC-004` and `SRC-007` are no longer cited by any case.
- `SRC-035` now points to the screenshot of the Meta notice in `data/case-notes/Gaylan/Gaylan1.jpeg`; `retrieved_at` set.
- Project title unified across `datapackage.json`, `LICENSE.md`, `CITATION.cff` and README: "Erase on Demand: How Bad Actors Silence Independent Journalism".
- README: EU disclaimer names the European Education and Culture Executive Agency (EACEA), which manages the CERV programme; outdated report date removed.
- `methodology.md` §2: episodes are separate rows linked by `campaign_id`, as in the data.
- `CITATION.cff`: individual authors added.
- `docs/data-readiness-audit.md` marked as a historical snapshot.

### Added
- Sources `SRC-055` (Qurium, 2021-04-12) and `SRC-056` (The Elephant, 2021-04-13).

---

## [1.0.2] - 2026-11-18

### Added
- `ELIM-009`: Google Search episode of the 2021 Maka Angola campaign (DMCA notices sent to Google in the names of Esquerda.net and Global News); `ELIM-007` remains the domain registrar episode.
- Researcher verification records `SRC-043`–`SRC-048` (Lumen Database notices 19738319, 19997993, 38942439, 24360852, 24529477 and a Wayback Machine snapshot of the copied article in the Mogul Press case).
- Researcher verification records `SRC-049`–`SRC-054`: written confirmations from the affected newsrooms obtained in August 2026 (correspondence held in the closed evidence vault, not published).

### Changed
- `ELIM-002`, `ELIM-004`: source corrected from `SRC-004` (Qurium, November 2021, which does not cover these cases) to `SRC-002` (Qurium, "Dark Ops Undercovered: Episode II", April 2021); Lumen records added.
- `MOGUL-001`: `claimant_name_as_reported` set to LMG Media Group, as named in the DMCA notice; Lumen record and Wayback snapshot added.
- `SHISH-001`, `WEB-001`, `PJ-002`, `RESP-001`, `RESP-003`, `RESP-006`, `LMC-001`, `MON-001`, `MON-002`: researcher verification records linked.
- `SRC-002`, `SRC-008`: Wayback search patterns replaced with specific snapshots; `SRC-008` title corrected (the article does not cover The Elephant).
- README Known Limitations updated (34 episodes, 32 `Confirmed`).

---

## [1.0.1] - 2026-10-14

### Changed
- `Confirmed` now also covers independent verification by a researcher (a preserved Wayback Machine snapshot, a Lumen Database record, or direct contact with the affected newsroom); README, `methodology.md` and `verification-protocol.md` aligned.
- ARES-001: replaced SRC-002 with CPJ (SRC-040); summary now records the Scribd and Dropbox removals.
- ARES-002: `Confirmed` → `Unverified`; SRC-002 replaced with Free Beacon (SRC-041) and Techdirt (SRC-042); `appeal_outcome` and `date_end` set to `unknown` (no source documents restoration); `date_start` set to 2013-11.
- ARES-003: `Confirmed` → `Unverified`; SRC-001 (published before the episode and not mentioning Plan V) replaced with CPJ (SRC-040); `platform` set to `unknown`.
- SRC-002: publication date corrected to 2021-04-20; no longer cited by any case.
- ACT-004: corrected note — Chevron was a target of Ares Rights notices, not a client.

### Added
- Sources SRC-040 (CPJ, 2016), SRC-041 (Free Beacon, 2013), SRC-042 (Techdirt, 2013).
- `platform = unknown` and the `source_type` values in use, including `researcher_verification`, documented in `codebook.md` and `datapackage.json`.

---

## [1.0.0] - 2026-10-03

### Added
- **Core Dataset (`data/cases.csv`)**: Initial standardized release featuring 33 platform enforcement episodes (all coded `Confirmed`; see README Known Limitations) targeting independent media across Kazakhstan, Angola, Peru, Georgia, Spain, Iran, and Latin America.
- **Sources Registry (`data/sources.csv`)**: 39 cross-referenced primary and secondary sources (SRC-031 and SRC-032 held in the closed evidence vault; SRC-035 links to the MP's public statement), including Lumen Database notices, media statements, and Qurium digital forensics reports.
- **Comparative Registry (`data/comparative_cases.csv`)**: 5 contextual cases documenting Telegram incidents, RTBF/defamation campaigns (PrimaDaNoi), and vendor repeat-offender signals (AiPlex K-pop/Spider-Man).
- **Frictionless Data Package (`datapackage.json`)**: Machine-readable schema specification covering all CSV tables, types, primary keys, and foreign-key relationships.
- **Documentation Suite (`docs/`)**:
  - `codebook.md`: Controlled vocabularies, field definitions, and the 6-point Platform Failure Framework (`FC-1` to `FC-6`).
  - `methodology.md`: Research scope, legal boundaries under the EU Digital Services Act (DSA), and verification criteria.
- **Repository Health & Governance**:
  - `LICENSE.md`: Dual CC-BY 4.0 (data & text) and MIT (scripts/tooling).
  - `CONTRIBUTING.md`: Submission workflows and guidelines for new cases and evidence.
  - `SECURITY.md`: Responsible disclosure policy and Evidence Vault data protection rules.

### Also added
- **Actors Registry (`data/actors.csv`)**: 29 actors (vendors, targets, platforms).
- `docs/roadmap-v1.0.md`, `scripts/validate.py`, CI workflow, `CITATION.cff`.

### Changed
- Corrected record counts in `docs/data-readiness-audit.md` (33 cases, not 35).
- Aligned `datapackage.json` version with release (1.0.0).
- Added public source links to `data/sources.csv` and registered SRC-037 to SRC-039; replaced placeholder `sender_volume_evidence` text in AIPLEX-001, RESP-004, RESP-005, LMC-002 and LMC-003 with source links; linked SRC-037 to GAYLAN-001.
- Reclassified AIPLEX-001 as `Confirmed`; target recorded as TVwithThinus and other uploaders of ANN7 clips (`independent_journalist_project`), motive `commercial_reputation_scrubbing`, summary rewritten.
- Updated README: episode definition (one row per platform episode, grouped by `campaign_id`), repository structure, and Known Limitations (closed-vault notices, inferred attribution for LMC-002/LMC-003, vendor name in a notice is not conclusive proof of who filed it).
- Clarified Google Transparency Report metrics for vendor AiPlex: standardized on **37%** of flagged URLs not present in Google Search index, correcting earlier preliminary estimates.
- Refactored granularity model: unified long-running cross-platform attacks via `campaign_id` while maintaining discrete platform episodes as individual `case_id` rows.
