# Methodology

## 1. Purpose

This methodology documents how cases are identified, verified, classified,
and included in the "Erase on Demand" dataset. It exists so that any external
researcher, journalist, or platform-accountability body (including EU DSA
enforcement units) can audit and reproduce the dataset's conclusions.

## 2. Unit of observation

The unit of observation is a **case**: a documented episode, or connected
series of episodes, in which a platform enforcement mechanism (copyright,
trademark, privacy/GDPR notice-and-action, or hosting/registrar takedown) was
used against the account, channel, page, or content of a media outlet, media
project, or civil society/press-freedom organization.

A single case may contain multiple **episodes** — distinct dated actions on
one or more platforms (e.g., a Facebook page removal in January followed by
an Instagram restriction in March against the same target). Episodes are
recorded within the case record rather than as separate top-level rows,
unless the mechanism, claimant, or platform differs enough to warrant
independent tracking and cross-referencing via a shared `campaign_id`.

## 3. Inclusion criteria

A case is included in `data/cases.csv` only if it satisfies all four
conditions below.

1. **Institutional target.** The affected account belongs to a media outlet,
   a named and identifiable media project, or a civil society/press-freedom
   organization. Personal accounts of individual journalists are excluded
   unless the account is the primary official channel of a media project.
2. **Enforcement mechanism.** The action relies on a platform's
   notice-and-action pipeline — copyright, trademark, privacy/GDPR, or a
   hosting/registrar abuse process — rather than on hacking, DDoS, or
   litigation outside the platform.
3. **Observable platform action.** The platform removed content, issued a
   strike, restricted, suspended, or deactivated the account or channel; or a
   primary source such as the Lumen Database documents that a notice was
   filed and is technically confirmed, even where the ultimate outcome is not
   yet known (coded as `platform_action = unknown`).
4. **Minimum identifiability.** The target, platform, an approximate date,
   the claimed legal basis, and at least one verifiable source can be
   established.

Confirmed unsuccessful takedown attempts — where the platform reviewed and
rejected the notice without restricting the target — are excluded from the
main dataset and are instead noted as context, since they do not demonstrate
platform failure.

## 4. Exclusion boundaries

The following categories are explicitly out of scope for the main dataset,
regardless of how well documented they are:

- **Telegram.** Telegram publishes no transparency reporting and offers no
  audit trail comparable to Meta or Google; incidents are described in
  narrative context only, never coded as dataset rows.
- **Personal, non-institutional accounts.** Attacks on an individual
  journalist's private account are tracked as narrative context unless that
  account functions as the primary channel of a media project.
- **DDoS and account compromise.** Infrastructure attacks are a distinct
  threat category outside this project's mandate.
- **SLAPP and defamation litigation, surveillance.** These are legal or
  physical-security threats, not platform enforcement abuse, and are excluded
  unless directly tied to a takedown notice.
- **Deepfakes and account cloning.** Included only where the clone or fake
  identity was itself submitted as "evidence" supporting a takedown request;
  otherwise treated as separate disinformation context.
- **False death reports.** Excluded as a distinct moderation-abuse category
  outside the IP/enforcement mandate.
- **Right-to-be-forgotten / GDPR de-indexing disputes not tied to takedown
  fraud** (e.g., PrimaDaNoi). These illustrate a structurally similar
  platform-arbitration failure but are recorded in
  `data/comparative_cases.csv`, since the legal basis, actor, and remedy
  differ from copyright/trademark takedown fraud.

## 5. Evidence tiers

Each case must reference at least one source before inclusion. Where
possible, the following primary evidence is sought and stored (either
publicly cited or, where it contains personal data, retained in a closed
evidence vault referenced by ID):

- Full text of the platform notice.
- Notice, case, strike, or complaint ID.
- The URL of the removed content and of the claimed "original" work.
- The claimant name and affiliation as shown by the platform.
- The type of claimed basis (copyright, trademark, privacy, other).
- Date of restriction and scope (single post, page, or full account).
- Text of any appeal or counter-notice and its outcome.
- Date and completeness of restoration, if any.
- A second, independent source, or an explicit note of why one is
  unavailable.

For suspected backdated-article schemes, additional forensic evidence is
collected: Wayback Machine captures, first known indexing date, WHOIS/RDAP
records for the mirror domain, DNS history, and a preserved copy of the fake
publication.

See `docs/evidence-checklist.md` for the full per-case checklist.

## 6. Verification and confidence levels

Every factual claim, not just every case, receives an independent confidence
rating:

- **Confirmed** — corroborated by two or more independent sources.
- **Unverified** — supported by a single source.
- **Plausible** — consistent with an established pattern but not directly
  evidenced.

A confirmed platform removal does not automatically confirm who filed the
notice, why, or on whose behalf. Attribution claims (e.g., "Vendor X acted on
behalf of Client Y") are rated separately from the underlying removal event.
Where a notice is filed under an individual's name with a claimed corporate
affiliation (e.g., a company domain in the sender's email address), the
dataset separates:

- the name as it appears in the notice (`claimant_name_as_reported`),
- the claimed affiliation (`claimant_affiliation`),
- whether the sender's identity was independently verified
  (`claimant_identity_verified`), and
- whether the affiliated organization has confirmed or denied involvement
  (`vendor_attribution`).

See `docs/verification-protocol.md` for the full source-verification
protocol.

## 7. Data sources

- **Lumen Database** — notice-level records filtered by sender, domain, date,
  and content type, used to identify patterns of mass or automated filing.
- **Google Transparency Report** — reporter-level copyright removal
  statistics, including URLs requested, delisted, and not found in the index.
- **DSA Transparency Database** — statements of reasons filed by platforms
  under Article 24(5) DSA.
- **Corporate registries** — India's MCA, UK Companies House, the
  Netherlands' KvK, and other national registries, used to map vendors'
  legal structures and corporate relationships.
- **Forensic reporting** — Qurium Media Foundation, Forbidden Stories, OCCRP,
  CPJ, RSF, and Access Now.
- **Direct evidence from affected newsrooms** — original notices, screenshots,
  and correspondence supplied by the affected organization.

## 8. Aggregate metrics vs. case-level claims

Aggregate figures describing a sender's overall behavior (for example, the
share of a reporter's requested URLs not found in Google's index) are stored
separately from individual case rows, together with the exact retrieval date,
reporter ID, and reporting period. This prevents a single aggregate statistic
from being silently reused across unrelated cases or across different time
windows, and ensures that corrections to an aggregate figure (for example,
where an earlier internal estimate is superseded by a verified figure drawn
directly from the platform's own transparency reporting) do not require
rewriting individual case records.

## 9. Updates and corrections

Every case record carries a `last_verified` date. When new evidence changes a
case's classification, confidence level, or attribution, the change is logged
in `CHANGELOG.md` rather than silently overwritten, preserving an audit trail
consistent with the project's evidentiary standards.
