# Erase on Demand: How Bad Actors Silence Independent Journalism

This repository documents verified cases of abuse of platform content-moderation
and notice-and-takedown systems used to silence independent media, journalists'
organizations, and civil society groups. The project is developed by Provereno
Media under the Tech Accountability Grants program (EFCSN / CERV, GA 101236606).

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

Long-running campaigns against a single target are recorded as one case with
multiple dated episodes, rather than as separate rows, to keep the dataset
easy to navigate.

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
  cases.csv               Main dataset: one row per case, with dated episodes
  comparative_cases.csv   Context/comparative cases outside the main scope
  sources.csv             Source registry with verification metadata
  datapackage.json         Frictionless Data Package descriptor
docs/
  methodology.md           Full research methodology
  codebook.md              Field definitions and controlled vocabularies
  verification-protocol.md Source verification and attribution rules
  evidence-checklist.md    Minimum evidence package per case
  data-readiness-audit.md  Status of each candidate case
case-notes/
  *.md                     Short narrative case files
CHANGELOG.md
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
