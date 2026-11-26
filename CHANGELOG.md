# Changelog

All notable changes to the **Erase on Demand** dataset, codebooks, and repository documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added (site, 2026-11-25): context cases
- New "Context cases" section on the site, loaded from `comparative_cases.csv`: cards with type, country, period, the reason for exclusion, and expandable summary and sources; type filter; pointer below the cases table; "Context" item in the navigation; `comparative_cases.csv` linked in the footer. Context cases are not counted in the site's figures, filters or charts.
- `CTX-TG-001` recoded from `personal_journalist_attack` to the new `threat_type` value `excluded_platform` (Telegram is out of scope; the target is a newsroom, not a personal account).

### Changed (data, 2026-11-25): context-case sources; AsiaTerra
- `comparative_cases.csv`: free-text `source_urls` replaced by `source_ids` referencing `sources.csv` (schema, codebook §2.1 and `validate.py` updated; the validator now checks context-case sources).
- Context cases re-checked against sources (SRC-065–SRC-076):
  - `CTX-RTBF-001`: demands were addressed to PrimaDaNoi, not Google (~240 demands, ~40 in court); period corrected to 2008–2018, ECtHR ruling 2021.
  - `CTX-UZ-001`: grounds corrected (mostly copyright complaints, some from impersonating profiles); AsiaTerra moved to the main dataset.
  - `CTX-TG-001`: dates and topic of the removed posts added from the newsroom's Telegram post.
  - `CTX-REC-001`: limited to the January 2019 K-pop removals; the 2018 Spider-Man Content ID error was not attributed to AiPlex and is dropped.
  - `CTX-PERS-001`: claims about clone channels and login attempts removed (not supported by the cited source).
- New episodes `ASIATERRA-001` (Facebook page removed early April 2026, later restored; `Confirmed`) and `ASIATERRA-002` (removed again on 9 May 2026; `Unverified`), campaign `CAMP-ASIATERRA-2026`.
- README dataset counts updated (37 episodes, 24 campaigns).

### Added (data, 2026-11-25): European targets
- `LEMONDE-001` (new campaign `CAMP-LEMONDE-STORYKILLERS-2024`): DMCA complaint signed "Jonesburg Law & Co." delisted Le Monde's Story Killers investigation into Team Jorge from Google Search, 28 March 2024; restored after a counter-notice. Coded `Confirmed`: La Marea (SRC-063) and the Lumen record checked by a researcher (SRC-064, `researcher_verification`). The sender is unattributed; `motive_category` is coded `commercial_reputation_scrubbing` as the closest available value.
- `CTX-MT-001` in `comparative_cases.csv`: copyright complaints to Google against Maltese websites covering the state hospitals privatisation deal, from March 2024 (Times of Malta, May 2024; EDMO/MedDMO, January 2025). Kept as context until target outlets and notices are identified in Lumen.
- New sources SRC-063 (La Marea, 18 June 2024) and SRC-064 (Lumen notice 40471185, researcher-checked).
- New `threat_type` value `unattributed_takedown` (`codebook.md` §2.1).
- README dataset counts updated (35 episodes, 23 campaigns, 33 `Confirmed`); Lumen checks for LEMONDE-001 and Malta added to the Priority Research Queue.

### Changed (CI, 2026-11-25): Pages workflow
- `pages.yml` split into `build` and `deploy` jobs (`deploy` needs `build`), so the deploy step no longer queries the `github-pages` artifact in the same job that uploaded it — the cause of the failed run 45219250948 ("No artifacts named github-pages were found").
- The site is now also built (not deployed) on pull requests that touch `site/`, `data/` or the workflow.
- Actions updated to Node 24 majors: `checkout@v7`, `configure-pages@v6`, `upload-pages-artifact@v5`, `deploy-pages@v5`. Deploys to the `github-pages` environment are no longer cancelled mid-run by a newer push.

### Changed (data, 2026-11-24): restoration status, Kazakhstan cluster
- `RESP-001`: `appeal_outcome` `permanent_loss` → `restored_editorial_appeal` (page restored after an RSF intervention, confirmed by a Provereno researcher; SRC-062).
- `LMC-002`: `appeal_outcome` `unknown` → `restored_editorial_appeal`; `date_start` set to 2026-04-16; summary records that Meta's notice reportedly cited fraud and deception (SRC-057). `failure_points` gains `FP6`, and `dsa_articles_implicated` is updated accordingly (§1.2.10).
- `SHISH-001`: `appeal_outcome` `unknown` → `permanent_loss`, as in the case note; `failure_points` gains `FP6`, and `dsa_articles_implicated` gains Article 20.
- `RESP-006`: `appeal_outcome` `unknown` → `partially_restored` (SRC-060, SRC-061).
- `RESP-002`, `RESP-003`: `appeal_outcome` unchanged (`not_appealed`); summaries record the restoration claimed by the newsroom and by Authentix (SRC-058, SRC-059), pending confirmation with the newsroom.
- New sources SRC-057 to SRC-062.
- New `appeal_outcome` value `partially_restored` (`codebook.md` §1.2.8, `datapackage.json`).
- Case notes (Respublika, Legal Media Centre), `Respublika_attack_waves_dataset.xlsx` (W02, W03, W04, W09) and `docs/data-readiness-audit.md` updated to match.

### Repository
- `SECURITY.md` and `CONTRIBUTING.md`: single contact address `info@provereno.media`; PGP line removed; response time "as soon as possible, normally within 5 working days".
- `SECURITY.md`: new section 4, "Corrections and Right of Reply" (referenced from README Known Limitations); names of private individuals added to "What is Published Publicly", as in README.
- Added the issue templates `Case Proposal` and `Evidence / Correction` (`.github/ISSUE_TEMPLATE/`), which `CONTRIBUTING.md` already referred to but which did not exist.

---

## [1.0.6] - 2026-11-18

### Changed
- Names of private individuals reworded to state only what the sources show:
  - `ACT-029`: renamed `Ripu Singh (name in YouTube notice)`; "Aditya Singh" is recorded only as the name under which the WhatsApp number is listed in a phone directory, per OCCRP/Monitori; the unsourced `parent_company` value "AiPlex (inferred sub-contractor)" removed.
  - `MON-001`: `claimant_name_as_reported` and `summary` reworded accordingly.
  - `LMC-001`: claimant recorded as the account name quoted by the foundation (Factcheck.kz, 23 Feb 2026); `claimant_identity_verified` set to `no`.
  - Case notes for Monitori, Legal Media Centre and Webamooz reworded to match; the Webamooz note no longer names an individual from closed-vault material.
- `codebook.md`: `self_admitted_sub_contractor` covers acknowledged work for a third party, named or not (as in MON-001).
- README Known Limitations: new item on names of private individuals.
- `docs/data-readiness-audit.md`: actor and claimant labels aligned with the above.

## [1.0.5] - 2026-11-18

### Fixed
- `SHISH-002`: `claimant_name_as_reported` now gives the claimant exactly as shown in the Instagram notice (`MR. ABHISHEK DHORELIYA SOLE PROPRIETOR OF MA…`, truncated by the platform); the surname was previously misspelled "Dhorelia".
- MarkScan domain corrected from `marcscan.in` to `markscan.in` (the notice gives `internet.enforcement@markscan.in`) in `SHISH-002`, `ACT-002`, `SRC-014` and `docs/data-readiness-audit.md`.
- `ACT-001`: the note no longer links AiPlex to the SHISH-002 notice, which does not name AiPlex; it now refers to the MarkScan domain address in the AiPlex notices of `RESP-004`/`RESP-005` (closed vault), as stated in README Known Limitations.
- `codebook.md`: the `claimant_name_as_reported` example no longer uses a private individual's name; truncated platform text is kept as displayed and marked as truncated.

### Site
- Page title set to the study title; links to methodology, codebook and repository now point to `Provereno-Media/Erase-On-Demand-Bad-Actors-VS-Journalists`.
- Funding block added above the footer: logos of the EU (co-funding), EFCSN and Provereno, in that order. Logo files are in `site/assets/`.
- "About this research": funding programme renamed to the EU Citizens, Equality, Rights and Values (CERV) programme (via EFCSN, https://efcsn.com/cerv-2026/), replacing "Tech Accountability Grants"; the EACEA disclaimer (as in `README.md`) moved into this block.
- "Narrative report" note added to "About the data"; the link will be added on publication.
- Case details: duplicate "DSA articles coded" line removed; `failed_control` values separated with ", ".

### Repository
- 1.0.0 marked as released (the "planned" label removed). Git tags `v1.0.0`–`v1.0.6` mark the repository state of each data release.
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
