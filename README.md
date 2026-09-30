# Erase on Demand: How Bad Actors Silence Independent Journalism

This repository documents verified cases of abuse of platform content-moderation
and notice-and-takedown systems used to silence independent media, journalists'
organizations, and civil society groups. The project is developed by Provereno
Media under the [Tech Accountability Grants program](https://efcsn.com/funding-opportunities/winners-tech-accountability-grants/) by the European Fact-Checking Standards Network.

## Interactive Dataset

[The interactive auto-updated dataset is available as a GitHub Page](https://provereno-media.github.io/Erase-On-Demand-Bad-Actors-VS-Journalists/)

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
  roadmap-v1.0.md          Roadmap for version 1.0
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

- **Confirmed** — corroborated by two or more independent sources.
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

See `CONTRIBUTING.md` for how to propose a case, submit evidence, or report a
correction.

## Known Limitations (v1.0.0)

- 33 episodes in 22 campaigns: 32 `Confirmed`, 1 `Unverified` (`AIPLEX-001`: the affected accounts are not identified).
- MON-001, GAYLAN-001 and RESP-001 rely on a limited number of independent sources; see `docs/data-readiness-audit.md`. For GAYLAN-001, three of the four listed sources point to the same public statement by the MP.
- `SRC-031` and `SRC-032` (Meta notices naming AiPlex in `RESP-004` and `RESP-005`) are held in the closed evidence vault and are not publicly archived. `SRC-035` currently links to the MP's public statement, not to the Meta notice itself, and its `retrieved_at` remains `PENDING`.
- AiPlex attribution for `LMC-002` and `LMC-003` is inferred from timing (`SRC-033`, `SRC-034`); no primary Meta notice was obtained.
- `SRC-038` and `SRC-039` have no archive link or publication date, and many `archive_url` values are Wayback search patterns rather than specific snapshots.
- Corporate registry records not yet obtained for Ares Rights, Initiatrix Technologies, Bytescare, Mogul Press and MarkScan; a MarkScan–AiPlex corporate link is not established.
- In episodes involving AiPlex and MarkScan, the sources document removals based on unfounded or unverified notices, but the vendor named in a notice is not conclusive proof of who actually filed it. In the Respublika.kz.media episodes `RESP-004` and `RESP-005`, notices naming AiPlex as claimant also contained a MarkScan domain address; the notices are held in the closed evidence vault and are not publicly archived (`SRC-031`, `SRC-032`). This research does not investigate the activities of these companies: its subject is the platform rules and mechanisms that both named and anonymous bad-faith claimants can exploit.
- Vendor attribution is reported as coded in `vendor_attribution`; it is not a legal finding.

Run `python3 scripts/validate.py` to check dataset integrity.
