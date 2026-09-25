# Codebook: Field Definitions and Controlled Vocabularies

This document defines the schema, field definitions, data types, and controlled vocabularies for all tabular datasets in the "Erase on Demand" repository:
- `data/cases.csv` (Primary Case Dataset)
- `data/actors.csv` (Actors Registry)
- `data/comparative_cases.csv` (Contextual and Comparative Cases)
- `data/sources.csv` (Evidence and Source Registry)

---

## 1. Primary Dataset: `data/cases.csv`

The primary dataset documents observed episodes where platform notice-and-action or enforcement mechanisms were used against the accounts, channels, pages, or content of media outlets, media projects, and civil society organizations.

### 1.1 Field Definitions and Types

| Field Name | Type | Required | Description |
|---|---|---|---|
| `case_id` | String | Yes | Unique identifier for the case (e.g., `ARES-001`, `RESP-001`, `PJ-001`). Primary key. |
| `campaign_id` | String | Yes | Cross-referencing identifier connecting related cases/episodes across time, platforms, or related targets (e.g., `CAMP-RESPUBLIKA-2026`). |
| `target_name` | String | Yes | Name of the targeted media outlet, media project, or civil society organization (e.g., `Respublika`, `Prosto Zhurnalistika`, `Legal Media Center`). |
| `target_type` | Enum | Yes | Classification of the targeted entity. Controlled vocabulary (see §1.2.1). |
| `target_country` | String (ISO 3166-1 alpha-2) | Yes | Country of origin/operation of the target (e.g., `KZ`, `UZ`, `EC`, `AO`). |
| `platform` | Enum | Yes | Platform or service provider where the enforcement action occurred. Controlled vocabulary (see §1.2.2). |
| `account_or_asset` | String | Yes | Specific handle, channel name, page title, or domain affected (e.g., `@respublika.kz.media`, `YouTube Channel`, `dropbox.com/s/...`). |
| `date_start` | String (YYYY-MM-DD) | Yes | Date when the takedown notice was filed or platform action was first observed. |
| `date_end` | String (YYYY-MM-DD or `unknown`) | No | Date when content/account was restored or appeal process was concluded. If ongoing or permanent, see `appeal_outcome`. |
| `enforcement_basis` | Enum | Yes | Legal or policy basis invoked in the complaint. Controlled vocabulary (see §1.2.3). |
| `abuse_mechanism` | Enum | Yes | Specific tactical mechanism used to manipulate platform moderation. Controlled vocabulary (see §1.2.4). |
| `motive_category` | Enum | Yes | Apparent strategic driver or objective behind the takedown. Controlled vocabulary (see §1.2.5). |
| `claimant_name_as_reported` | String | Yes | Name of the complainant exactly as displayed in the notice or platform notification (e.g., `Abhishek Dhorelia`, `Ares Rights`, `Giorgio Armani`). |
| `claimant_affiliation` | String | Yes | Corporate or organizational affiliation claimed by the sender (e.g., `MarkScan`, `AiPlex`, `Self-employed`). |
| `claimant_identity_verified` | Enum | Yes | Independent verification status of the individual sender's identity. Controlled vocabulary (`yes`, `no`, `unknown`). |
| `vendor_attribution` | Enum | Yes | Evidentiary status linking the takedown to a commercial reputation/copyright vendor. Controlled vocabulary (see §1.2.6). |
| `high_volume_sender` | Enum | Yes | Whether the sender demonstrates industrial/mass notice generation. Controlled vocabulary (`yes`, `no`, `unknown`). |
| `sender_volume_evidence` | String | No | Verifiable citation or data point supporting `high_volume_sender` (e.g., `Google Transparency Report reporter ID 40866: 13.1M URLs`). |
| `platform_action` | Enum | Yes | Action taken by the platform against the target. Controlled vocabulary (see §1.2.7). |
| `appeal_outcome` | Enum | Yes | Final observed status following counter-notice or editorial appeal. Controlled vocabulary (see §1.2.8). |
| `failed_control` | String | Yes | Platform systemic control failure points. Comma-separated enum values (see §1.2.9). |
| `dsa_articles_implicated` | String | No | Articles of Regulation (EU) 2022/2065 (DSA) relevant to the failure. Comma-separated list (e.g., `17, 20, 34, 35`). |
| `confidence` | Enum | Yes | Overarching evidentiary confidence of the case. Controlled vocabulary (`Confirmed`, `Unverified`, `Plausible`). |
| `summary` | String | Yes | Concise factual summary of the episode (1–3 sentences). |
| `source_ids` | String | Yes | Semicolon-separated identifiers referencing records in `data/sources.csv` (e.g., `SRC-001; SRC-004`). |
| `last_verified` | String (YYYY-MM-DD) | Yes | Date when records and sources for this entry were last reviewed. |

---

### 1.2 Controlled Vocabularies for `cases.csv`

#### 1.2.1 `target_type`
- `investigative_media`: Independent investigative newsroom or news organization.
- `civil_society_ngo`: Non-governmental organization, human rights or press freedom defender.
- `independent_journalist_project`: Formal editorial media project run under a named journalist's banner (e.g., *Prosto Zhurnalistika*).
- `commercial_media`: General interest or commercial news publisher.
- `corporate_litigant`: Non-media corporate entity targeted in public interest litigation (exceptionally approved case, e.g., Chevron in Ecuador).

#### 1.2.2 `platform`
- `facebook`: Meta Facebook (Pages, Profiles, Groups).
- `instagram`: Meta Instagram.
- `youtube`: Google YouTube.
- `google_search`: Google Web Search (delisting / de-indexing).
- `hosting_provider`: Web hosting infrastructure provider (e.g., DigitalOcean, AWS).
- `cloud_storage`: Cloud file hosting / distribution service (e.g., Dropbox, Scribd).
- `domain_registrar`: Domain registrar or DNS provider (e.g., easyDNS).

#### 1.2.3 `enforcement_basis`
- `copyright`: Claimed infringement of copyright, audio/video rights, or DMCA takedown.
- `trademark`: Claimed unauthorized use of trademark, company logo, or brand identity.
- `gdpr_privacy`: Claimed violation of data protection laws, right to be forgotten, or privacy rights via notice-and-takedown.
- `community_standards`: False reporting under ToS/Community Guidelines (e.g., adult harassment, hate speech, spam) used in coordination with IP claims.
- `other_ip`: Other intellectual property provisions.

#### 1.2.4 `abuse_mechanism`
- `fictitious_rights_claim`: Claimant asserts ownership of materials they do not own and could not legitimately hold rights to.
- `backdated_article`: Original article is copied to a disposable or backdated third-party domain, which is then submitted as the "original" to claim the legitimate article is infringing plagiarism.
- `legitimate_looking_bad_faith`: Notice formally conforms to legal requirements or uses existing trademarks/copyrights as a pretext to censor public-interest critique.
- `impersonation_claimant`: Notice filed using the stolen identity of a real media organization, company, or third party without their authorization.
- `fake_corporate_entity`: Notice submitted by a fabricated shell entity (e.g., generic templates such as "[Name] Media Corporation").
- `prior_upload_scheme`: Third-party captures public-domain, creative commons, or editorial media, uploads it to a throwaway account shortly before filing, and claims infringement.
- `automated_mass_filing`: High-frequency, algorithmic filing of claims without human verification of legality or fair-use context.

#### 1.2.5 `motive_category`
- `political_state_censorship`: Suppression of investigative reporting, dissent, or criticism by or on behalf of government officials.
- `fraudster_protection`: Deletion of public records and investigations concerning financial scams, fraud, or money laundering.
- `commercial_reputation_scrubbing`: Commercial contract service hired to purge negative reporting about wealthy individuals or businesses.
- `activism_suppression`: Silencing human rights monitoring, environmental defense, or press-freedom activism.
- `parliamentarily_recognised_censorship`: Takedown campaign formally identified and denounced in a parliamentary proceeding, official government statement, or regulatory body ruling as politically motivated censorship (e.g., UK Parliament Early Day Motion, EU Parliament question, national parliamentary committee finding).
- `reputation_vendor_self_defense`: Takedowns directed against reports exposing the takedown vendors themselves (e.g., AiPlex notices against Techdirt).

#### 1.2.6 `vendor_attribution`
- `confirmed`: Attribution to a specific vendor/entity is established by direct domain email headers, admission, corporate registry link, or judicial/regulatory finding.
- `claimed_affiliation`: Complainant used vendor's corporate name or domain in the notice, but third-party identity theft or spoofing cannot be completely excluded without raw headers.
- `technical_forensic_attribution`: Attribution established via digital forensics (metadata analysis, shared network infrastructure, Lumen pattern clustering).
- `self_admitted_sub_contractor`: Individual or entity has publicly or semi-publicly acknowledged working as a sub-contractor, affiliate, or agent for a named vendor, establishing a non-disputable contractual relationship without constituting a full `confirmed` corporate-level attribution (e.g., LinkedIn profile, marketplace listing, or court declaration).
- `unattributed_proxy`: Notice submitted through disposable personal emails, shell entities, or proxies with unknown commercial ownership.

#### 1.2.7 `platform_action`
- `content_removal`: Specific post, article, URL, video, or image removed or delisted.
- `account_deactivation`: Full user account, Facebook Page, or Instagram account suspended, disabled, or deleted.
- `channel_termination`: YouTube channel completely removed.
- `feature_restriction`: Account restricted from posting, advertising, or discovery.
- `strike_issued`: Official penalty/strike logged against the account without immediate total termination.
- `service_interruption`: Hosting provider or registrar suspended domain/server access.
- `unknown`: Technical submission of bad-faith notice is confirmed (e.g., via Lumen), but actual enforcement action on target URL could not be independently ascertained.

#### 1.2.8 `appeal_outcome`
- `restored_editorial_appeal`: Restored after informal pressure, high-level mediation, or direct outreach by civil society/NGO partners.
- `restored_formal_counternotice`: Restored via statutory DMCA counter-notification or formal platform appeal workflow.
- `rejected`: Platform formally reviewed and upheld the takedown or deactivation.
- `pending`: Appeal process is currently active or unresolved.
- `not_appealed`: Target did not or could not appeal (e.g., fear of jurisdiction submission, lack of technical capacity).
- `permanent_loss`: Account or material permanently removed with all appeal channels exhausted.
- `unknown`: Outcome of the appeal or current state of the content is unverified.

#### 1.2.9 `failed_control` (Structural Platform Failure Points)
- `lack_of_pre_action_verification`: Platform automated or processed notice without checking prima facie validity or target context.
- `asymmetric_burden_of_proof`: Platform demands onerous legal declarations or personal data from target while accepting unverified third-party claims.
- `flawed_appeal_pipeline`: Non-functional, automated, or circular internal complaint-handling system.
- `unverified_claimant_identity`: Platform allows filing using unverified disposable emails, spoofed identities, or fabricated legal entities.
- `disproportionate_enforcement`: Platform deactivates entire institutional accounts or history rather than evaluating isolated disputed items.
- `lack_of_trusted_channel_scrutiny`: Failure to audit or sanction high-volume repeat abusers utilizing privileged submission pipelines.

---

## 2. Comparative & Context Dataset: `data/comparative_cases.csv`

This dataset documents relevant incidents that illustrate structural moderation failures, legal disputes, or adjacent threat vectors, but fall outside the strict boundaries of `data/cases.csv` (e.g., RTBF legal orders, personal account strikes, non-enforcement attacks).

### 2.1 Schema

| Field Name | Type | Description |
|---|---|---|
| `context_id` | String | Unique identifier (e.g., `CTX-RTBF-001`, `CTX-UZ-001`). |
| `title` | String | Descriptive title of the case or incident group. |
| `period` | String | Time period or specific date (e.g., `2016–2021`, `March 2026`). |
| `country` | String (ISO 3166-1 alpha-2) | Geographic location of the target or events. |
| `threat_type` | Enum | Classification: `rtbf_gdpr_legal`, `personal_journalist_attack`, `disinformation_clone`, `slapp_litigation`, `mass_repetition_benchmark`. |
| `exclusion_reason` | String | Methodological reason why this entry is excluded from `cases.csv` (see `methodology.md` §4). |
| `summary` | String | Factual summary and relevance to platform accountability. |
| `source_urls` | String | Primary references or investigative reports. |

---

## 3. Evidence & Source Registry: `data/sources.csv`

The source registry provides full bibliographic and forensic provenance for every citation in `cases.csv` and `comparative_cases.csv`.

### 3.1 Schema

| Field Name | Type | Description |
|---|---|---|
| `source_id` | String | Unique source identifier (e.g., `SRC-001`). Primary key. |
| `source_type` | Enum | `lumen_notice`, `platform_transparency_report`, `court_filing`, `corporate_registry`, `investigative_report`, `newsroom_direct_evidence`, `press_release`. |
| `title` | String | Title of document, investigation, or notice. |
| `author_or_publisher` | String | Entity that authored or published the source (e.g., `Qurium`, `EFF`, `Lumen Database`, `OCCRP`). |
| `url` | String | Public web URL or archive permalink. |
| `archive_url` | String | Wayback Machine / Archive.today preserved link. |
| `vault_reference` | String | Internal ID for confidential/redacted evidence kept in closed vault (e.g., `VAULT-EML-2026-004`). |
| `date_published` | String (YYYY-MM-DD) | Publication or notice generation date. |
| `retrieved_at` | String (YYYY-MM-DD) | Date when evidence was collected and verified. |

---

## 4. Actors Registry: `data/actors.csv`

The actors registry provides a normalized lookup table of all organizations, individuals, and platforms referenced across `cases.csv`. Each actor receives a stable `actor_id` enabling cross-case analysis of repeat offenders, corporate structures, and platform roles. The registry is maintained independently of individual case records to avoid data duplication and to allow actors to be updated as new corporate OSINT evidence emerges.

### 4.1 Field Definitions and Types

| Field Name | Type | Required | Description |
|---|---|---|---|
| `actor_id` | String | Yes | Unique stable identifier for the actor (e.g., `ACT-AIPLEX-001`, `ACT-ARES-001`, `ACT-RESPUBLIKA-001`). Primary key. |
| `actor_name` | String | Yes | Canonical name of the actor as used in official registries or primary sources. |
| `actor_type` | Enum | Yes | Organizational or individual classification. Controlled vocabulary (see §4.2.1). |
| `actor_role` | Enum | Yes | Functional role of the actor within this dataset's analytical framework. Controlled vocabulary (see §4.2.2). |
| `jurisdiction` | String (ISO 3166-1 alpha-2) | Yes | Primary country of incorporation, operation, or citizenship (e.g., `IN`, `ES`, `KZ`, `GB`). |
| `registration_number` | String | No | Official corporate registration number from a primary government registry (e.g., MCA CIN, Companies House number, KvK number). |
| `registration_source` | String | No | Name of the registry from which `registration_number` was obtained (e.g., `India MCA`, `UK Companies House`, `Netherlands KvK`, `Kenya Companies Registry`). |
| `registration_url` | String | No | Direct URL to the actor's official registry entry. Should link to the primary government database, not a secondary aggregator. |
| `parent_company` | String | No | `actor_id` of the parent entity if the actor is a subsidiary, division, or controlled affiliate. |
| `known_clients` | String | No | Semicolon-separated list of known or alleged clients based on confirmed reporting or corporate disclosures (e.g., `Rosneft; Sberbank; [unnamed government agency KZ]`). |
| `privileged_platform_access` | Enum | No | Whether the actor holds or claims Trusted Partner, Trusted Flagger, or equivalent privileged submission status on any major platform. Controlled vocabulary (see §4.2.3). |
| `notes` | String | No | Additional context, links to pending OSINT tasks, or caveats about data reliability not captured by structured fields. |
| `last_verified` | String (YYYY-MM-DD) | Yes | Date when the actor record was last reviewed against primary sources. |

---

### 4.2 Controlled Vocabularies for `actors.csv`

#### 4.2.1 `actor_type`
- `company`: Incorporated legal entity (limited company, LLC, private limited, etc.).
- `individual`: Natural person acting in a professional capacity (e.g., freelance DMCA agent, sub-contractor).
- `media_outlet`: Established news organization with editorial staff and published output.
- `media_project`: Structured journalistic project operating under a named journalist or small team without full institutional status.
- `civil_society_ngo`: Non-governmental organization, advocacy group, or press freedom body.
- `platform`: Major internet platform or infrastructure provider subject to DSA or equivalent regulation.

#### 4.2.2 `actor_role`
- `vendor`: Commercial entity or individual providing reputation management, copyright enforcement, or link-removal services to clients.
- `target`: Media outlet, journalist project, or civil society organization that was the subject of an enforcement action in `cases.csv`.
- `platform`: Infrastructure provider that processed or executed the enforcement action.
- `claimant`: Individual or entity named as the formal complainant in a notice or filing, which may or may not be the originating vendor.

> **Note:** An actor may appear with multiple roles across different cases. For example, a vendor (`ACT-AIPLEX-001`) may also act as a direct `claimant` in specific notices. In such cases, the `actor_role` field records the actor's **primary** role in the dataset; cross-role appearances are captured through the `claimant_affiliation` field in `cases.csv`.

#### 4.2.3 `privileged_platform_access`
- `yes`: Actor demonstrably holds Trusted Partner, Trusted Flagger, or equivalent privileged submission status on at least one major platform, confirmed by platform disclosure or reliable third-party reporting.
- `no`: Actor has no known privileged access; notices filed through standard public submission channels.
- `claimed_but_unconfirmed_by_platform`: Actor publicly advertises or implies privileged platform access (e.g., marketing materials, client presentations), but the platform itself has not confirmed the status, or the platform's published Trusted Flagger/Partner lists do not include the actor.
- `unknown`: Insufficient evidence to determine access level.

> **DSA Relevance:** Under DSA Article 22, Trusted Flaggers must be established in the EU and awarded status by the relevant Digital Services Coordinator. Vendors advertising privileged access without verifiable EU establishment or official designation may constitute a misrepresentation relevant to Article 22 compliance assessments.
