# Changelog

All notable changes to the **Erase on Demand** dataset, codebooks, and repository documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-03 (planned)

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
