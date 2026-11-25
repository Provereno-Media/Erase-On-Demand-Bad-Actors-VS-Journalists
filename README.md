# Erase on Demand: How Bad Actors Silence Independent Journalism

This repository documents verified cases of abuse of platform content-moderation
and notice-and-takedown systems used to silence independent media, journalists'
organizations, and civil society groups. Provereno develops the project
Media under the EU [Citizens, Equality, Rights and Values (CERV) programme](https://efcsn.com/cerv-2026/) through the European Fact-Checking Standards Network (EFCSN).

**Co-funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Education and Culture Executive Agency (EACEA). Neither the European Union nor the granting authority can be held responsible for them.**
<img width="1200" height="257" alt="EU-logo" src="https://github.com/user-attachments/assets/c79d0e4a-2dcf-4546-88a4-68b2b6314a2d" />

## Interactive Dataset

**[The interactive auto-updated dataset is available as a GitHub Page](https://provereno-media.github.io/Erase-On-Demand-Bad-Actors-VS-Journalists/)**

## Narrative report

The narrative report will be published in English and Russian. A link will be added here on publication.

## What this project studies

The central object of analysis is not individual vendors (AiPlex, MarkScan,
Eliminalia, and similar actors) but the structural failure of platform
enforcement systems: privileged "trusted" reporting channels, automated
takedown pipelines that operate without content verification, and the absence
of effective oversight under the EU Digital Services Act (DSA).

The dataset documents observed episodes in which copyright, trademark, or
privacy/GDPR enforcement mechanisms on Meta, Google Search, YouTube, hosting
providers, and domain registrars were used to remove or restrict content
belonging to media outlets, media projects, and civil society organizations.

## Scope: what is included

A case qualifies for the main dataset (`data/cases.csv`) only if all of the
following are true:

1. **Target.** The affected account, page, channel, or content belongs to a
   media outlet, a named media project, or a civil society/press-freedom
   organization — not a private, non-institutional personal account.
2. **Mechanism.** The action relies on a platform enforcement mechanism:
   copyright, trademark, privacy/GDPR notice-and-action, or hosting/registrar
   takedown.
3. **Platform response.** The platform took an observable action — content
   removal, account/channel restriction, suspension, or deactivation — or a
   credible primary source (e.g., the Lumen Database) documents a notice whose
   outcome is not yet known.
4. **Minimum evidence.** The target, platform, approximate date, claimed
   basis, and at least one verifiable source are known.

Each row of `data/cases.csv` is one platform-level episode: a single
enforcement action against one account, page, channel, or content set.
Episodes that belong to the same campaign share a `campaign_id`.

## Scope: what is context only

The following material is documented in prose, in case notes, or in
`data/comparative_cases.csv`, but is **not coded** in the main dataset:

- Telegram-related incidents (Telegram publishes no transparency data and is
  treated as narrative context only).
- Attacks on personal, non-institutional accounts of individual journalists.
- Cases with insufficient detail to identify the mechanism, platform, or
  outcome.
- Right-to-be-forgotten / GDPR de-indexing disputes such as PrimaDaNoi, kept
  in a separate comparative table because they are not copyright/IP
  enforcement.
- DDoS attacks, account hacking, and other infrastructure-level attacks.
- SLAPP suits, defamation litigation, and surveillance, unless directly tied
  to a platform takedown.
- Account cloning and deepfakes, unless the clone was itself used as
  "evidence" to justify a takedown.
- False reports of a user's death submitted to a platform.
- Confirmed unsuccessful takedown attempts that produced no platform action.

## Repository structure

```
data/
  cases.csv               Main dataset: one row per platform episode;
                          episodes of one campaign share a campaign_id
  comparative_cases.csv   Context/comparative cases outside the main scope
  actors.csv              Vendors and intermediaries referenced in cases
  sources.csv             Source registry with verification metadata
  datapackage.json        Frictionless Data Package descriptor
  case-notes/             Short narrative case files (*.md) and supporting
                          materials
  Aiplex/, Google YT Search etc/,
  [Facebook] and [Instagram] DSA VLOP Transparency Report - 28 August 2026/
                          Source material folders
docs/
  methodology.md           Full research methodology
  codebook.md              Field definitions and controlled vocabularies
  verification-protocol.md Source verification and attribution rules
  evidence-checklist.md    Minimum evidence package per case
  data-readiness-audit.md  Status of each candidate case
scripts/
  validate.py              Dataset integrity check
site/
  index.html               Interactive dataset page
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
SECURITY.md
LICENSE.md
README.md
```

## Verification standard

Every case is coded with a confidence level:

- **Confirmed** — corroborated by two or more independent sources or verified
  independently by a researcher (a preserved Wayback Machine snapshot, a Lumen
  Database record, or direct contact between a researcher and the affected
  newsroom).
- **Unverified** — supported by a single source.
- **Plausible** — logically consistent with the pattern but not yet proven.

Confidence is assigned per claim, not only per case: a confirmed removal does
not imply a confirmed attribution of who filed the notice or why.

## Legal and ethical boundaries

This project makes no legal accusations. It documents observed facts and
qualifies them by confidence level. It does not conflate legitimate copyright
enforcement with abuse; the distinguishing criteria are the absence of a
credible legal basis, a pattern of mass or automated filing, and a connection
to politically or commercially sensitive content.

## License and data handling

See `LICENSE.md` for licensing terms covering code, data, and text. Personal
data contained in original takedown notices (private email addresses, phone
numbers) is not published in this public repository; a closed evidence vault
is maintained separately by the research team.

## How to contribute

We welcome contributions from investigative journalists, OSINT researchers, media lawyers, platform accountability advocates, and impacted newsrooms.

### Ways to Contribute

1. **Submit a New Case**: Propose an episode of takedown abuse against a media outlet or civil society organization.
2. **Provide Verifying Evidence**: Supply primary documentation (takedown notices, case IDs, headers, Lumen links, restoration notices) for existing cases marked `Unverified` or `Plausible`.
3. **Report Factual Errors / Corrections**: Notify us of inaccuracies in dates, claimants, URLs, or platform actions.
4. **Improve Data Infrastructure**: Contribute schema validation scripts, visualizers, or documentation improvements.

See `CONTRIBUTING.md` for how to propose a case, submit evidence, or report a
correction. 

## Known Limitations (v1.0.4) as of November 18, 2026

- 37 episodes in 24 campaigns: 34 `Confirmed` and 3 `Unverified` (ARES-002, ARES-003, ASIATERRA-002) as of November 25, 2026.
- Researcher verifications for single-source `Confirmed` episodes are recorded as `researcher_verification` entries in `data/sources.csv`: Lumen Database records and a Wayback Machine snapshot (`SRC-043`–`SRC-048`) and written confirmations from the affected newsrooms obtained in August 2026 (`SRC-049`–`SRC-054`). The newsroom correspondence is held in the closed evidence vault and is not published. `ELIM-007` (domain registrar episode) and `ELIM-008` remain `Confirmed` on the basis of `SRC-008` and `SRC-009` respectively, without a separate published `researcher_verification` entry.
- GAYLAN-001 and RESP-001 rely on a limited number of independent sources; see `docs/data-readiness-audit.md`. For GAYLAN-001, three of the four listed sources point to the same public statement by the MP; the fourth, `SRC-035`, is a screenshot of the Meta notice itself (`data/case-notes/Gaylan/Gaylan1.jpeg`).
- `SRC-031` and `SRC-032` (Meta notices naming AiPlex in `RESP-004` and `RESP-005`) are held in the closed evidence vault and are not publicly archived.
- AiPlex attribution for `LMC-002` and `LMC-003` is inferred from timing (`SRC-033`, `SRC-034`); no primary Meta notice was obtained.
- `SRC-038` and `SRC-039` have no archive link or publication date, and many `archive_url` values are Wayback search patterns rather than specific snapshots.
- In episodes involving AiPlex and MarkScan, the sources document removals based on unfounded or unverified notices, but the vendor named in a notice is not conclusive proof of who actually filed it. In the Respublika.kz.media episodes `RESP-004` and `RESP-005`, notices naming AiPlex as claimant also contained a MarkScan domain address; the notices are held in the closed evidence vault and are not publicly archived (`SRC-031`, `SRC-032`). This research does not investigate the activities of these companies: its subject is the platform rules and mechanisms that both named and anonymous bad-faith claimants can exploit.
- Vendor attribution is reported as coded in `vendor_attribution`; it is not a legal finding.
- Names of private individuals are reproduced only as they appear in platform notices or in published reporting (OCCRP/Monitori, Factcheck.kz), in their role as claimants. Inclusion does not establish a person's identity, and names shown in notices may be false or used without the named person's knowledge. Corrections: see SECURITY.md.

## AI Use Disclosure

The following large language models and AI tools were used in preparing this study:

- Perplexity Deep Research: for initial region-focused data collection on takedowns, and for preliminary identification of links between the companies behind the takedowns
- Gemma 4 E4B (locally deployed) and Claude Sonnet 5: for automated analysis of Lumen Database statistics and of Google’s and Meta’s own DSA compliance reports
- Tesari’s First Resort: for collecting data on the companies behind the takedowns and analyzing their connections
- Perplexity, Gemma 4 E4B (locally deployed), Claude Sonnet 5, GPT 6 Sol and Gemini 3.8 Flash: for normalizing and labeling the collected data before publishing it to the open repository
- Claude Opus 5.5: for configuring the interactive dashboard and for automating the ongoing addition of new cases to the repository structure
- Claude Fable 5.2: for the draft English translation of the study

All data were independently verified by the study’s authors and editors.
