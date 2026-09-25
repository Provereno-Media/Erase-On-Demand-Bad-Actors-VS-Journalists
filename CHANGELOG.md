# Changelog

All notable changes to the **Erase on Demand** dataset, codebooks, and repository documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-09-25

### Added
- **Core Dataset (`data/cases.csv`)**: Initial standardized release featuring 32 platform enforcement episodes targeting independent media across Kazakhstan, Angola, Peru, Georgia, Spain, Iran, and Latin America.
- **Sources Registry (`data/sources.csv`)**: 29 cross-referenced primary and secondary sources, including Lumen Database notices, media statements, and Qurium digital forensics reports.
- **Comparative Registry (`data/comparative_cases.csv`)**: 7 contextual cases documenting Telegram incidents, RTBF/defamation campaigns (PrimaDaNoi), and vendor repeat-offender signals (AiPlex K-pop/Spider-Man).
- **Frictionless Data Package (`datapackage.json`)**: Machine-readable schema specification covering all CSV tables, types, primary keys, and foreign-key relationships.
- **Documentation Suite (`docs/`)**:
  - `codebook.md`: Controlled vocabularies, field definitions, and the 6-point Platform Failure Framework (`FC-1` to `FC-6`).
  - `methodology.md`: Research scope, legal boundaries under the EU Digital Services Act (DSA), and verification criteria.
- **Repository Health & Governance**:
  - `LICENSE.md`: Dual CC-BY 4.0 (data & text) and MIT (scripts/tooling).
  - `CONTRIBUTING.md`: Submission workflows and guidelines for new cases and evidence.
  - `SECURITY.md`: Responsible disclosure policy and Evidence Vault data protection rules.

### Changed
- Clarified Google Transparency Report metrics for vendor AiPlex: standardized on **37%** of flagged URLs not present in Google Search index, correcting earlier preliminary estimates.
- Refactored granularity model: unified long-running cross-platform attacks via `campaign_id` while maintaining discrete platform episodes as individual `case_id` rows.
