# Data Readiness Audit

**Last updated:** 2026-09-25  
**Scope:** `data/cases.csv` (35 rows) and `data/actors.csv` (29 rows)  
**Purpose:** Track outstanding evidence gaps, verification priorities, and publication blockers for each case and actor record. Updated after each research sprint.

---

## How to Read This Audit

Each case row is assessed across five dimensions:

| Symbol | Meaning |
|--------|---------|
| ✅ | Complete — no action needed |
| ⚠️ | Partial — known gap, not a publication blocker |
| ❌ | Missing — blocks promotion to `Confirmed` or inclusion in policy outputs |
| 🔍 | Active research task |

**Dimensions assessed:**

1. **Claimant identity** — Is the claimant named and verified against primary sources?
2. **Vendor attribution** — Is the attribution to a vendor confirmed, claimed, or forensic?
3. **Platform action documented** — Is the outcome (removal, suspension, etc.) evidenced by a primary source?
4. **Appeal/restoration** — Is the appeal outcome known and sourced?
5. **Source count** — Minimum 2 independent sources for `Confirmed` confidence.

---

## Cases — Evidence Gap Matrix

### ARES cluster (Ares Rights / Ecuador)

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| ARES-001 | ⚠️ Ares Rights self-identified in notices; no corporate registry record in dataset | ⚠️ claimed_affiliation only | ✅ Content removed, restored on counter-notice | ✅ Restored | ✅ SRC-001; SRC-002 | 🔍 Obtain Spain BORME or US registry entry for Ares Rights |
| ARES-002 | ⚠️ Same as above | ⚠️ claimed_affiliation only | ✅ Videos removed, restored | ✅ Restored | ✅ SRC-001; SRC-002 | 🔍 Same as ARES-001 |
| ARES-003 | ⚠️ Same as above | ⚠️ claimed_affiliation only | ✅ Photos removed | ❌ Outcome unknown | ✅ SRC-001 | ❌ Single source; appeal outcome unknown |

**Cluster priority:** Obtain Ares Rights corporate registry record (Spain BORME or US state). Single-source status of ARES-003 does not block publication but limits confidence upgrade.

---

### AIPLEX cluster (AiPlex / ANN7)

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| AIPLEX-001 | ⚠️ AiPlex named in notices; identity not independently verified | ⚠️ claimed_affiliation + Google TR ID 40866 | ⚠️ Content removal reported; exact account IDs not confirmed | ❌ Unknown | ⚠️ SRC-003 only | ❌ Single source; target account status unconfirmed; confidence `Unverified` |

**Cluster priority (HIGH):** AIPLEX-001 is the only case at `Unverified` confidence. Required: (a) second independent source; (b) confirmation that target accounts exist/existed; (c) Google Transparency Report snapshot archived.

---

### ELIM cluster (Eliminalia)

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| ELIM-001 | ❌ Claimant unknown; Eliminalia identified by forensics only | ✅ technical_forensic_attribution (Qurium) | ⚠️ Suppression documented; no platform removal notification obtained | ❌ Unknown | ✅ SRC-004; SRC-005 | ⚠️ No platform confirmation of action; forensic attribution sufficient for `Confirmed` |
| ELIM-002 | ❌ Claimant unknown | ✅ technical_forensic_attribution | ⚠️ Backdated copy documented; no platform removal notice | ❌ Unknown | ✅ SRC-004 | ⚠️ Same as ELIM-001 |
| ELIM-003 | ❌ Claimant unknown | ✅ technical_forensic_attribution | ✅ Site unavailable ~1 week; documented | ❌ Unknown | ✅ SRC-004; SRC-006 | ⚠️ Appeal outcome unresolved |
| ELIM-004 | ❌ Claimant unknown | ✅ technical_forensic_attribution | ⚠️ Deindexing attempt documented; final removal status unclear | ❌ Unknown | ✅ SRC-004 | ⚠️ Platform action outcome unclear |
| ELIM-005 | ⚠️ Various purported entities; no real identity confirmed | ✅ technical_forensic_attribution | ⚠️ Hosting complaints documented | ❌ Unknown | ✅ SRC-004; SRC-007 | ⚠️ Claimant identity complexity warrants dedicated case note |
| ELIM-006 | ⚠️ Same pattern as ELIM-005 | ✅ technical_forensic_attribution | ⚠️ Hosting complaints documented | ❌ Unknown | ✅ SRC-004; SRC-007 | ⚠️ Same |
| ELIM-007 | ⚠️ Named orgs (Esquerda.net, O Globo) denied filing | ✅ technical_forensic_attribution | ⚠️ Domain complaint documented | ❌ Unknown | ✅ SRC-008 | 🔍 Obtain denial statements from named organizations as primary sources |
| ELIM-008 | ❌ Claimant unknown; vendor unattributed_proxy | ❌ unattributed_proxy — Eliminalia link not confirmed forensically | ✅ Removal + restoration documented | ✅ Restored | ✅ SRC-009 | ❌ Vendor attribution weak; second source needed to upgrade from unattributed_proxy |

**Cluster priority:** ELIM-008 is the weakest attribution in the Eliminalia cluster. ELIM-007 needs denial statements from named orgs. Remaining cases adequately covered by Qurium forensics.

---

### MOGUL / INITIATRIX / WEBAMOOZ (single-case clusters)

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| MOGUL-001 | ❌ Claimant unknown | ⚠️ claimed_affiliation (Mogul Press beneficiary, not confirmed filer) | ⚠️ DMCA complaint to Google documented; removal outcome unclear | ❌ Unknown | ✅ SRC-010 | ⚠️ Single source; platform outcome unclear. Not a blocker for current confidence level |
| INIT-001 | ❌ Fictitious identities; no real person identified | ✅ technical_forensic_attribution (Qurium) | ⚠️ Removal documented by target; no platform notice obtained | ❌ Unknown | ✅ SRC-011; SRC-012 | ⚠️ No platform-side confirmation; forensic attribution sufficient |
| WEB-001 | ⚠️ Bytescare named in notices | ⚠️ claimed_affiliation | ✅ Content removal and partial restoration documented | ✅ Partially restored | ✅ SRC-015 | 🔍 Obtain India MCA or other registry record for Bytescare |

---

### SHISHKIN LIKE cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| SHISH-001 | ⚠️ Purported Kazakh orgs denied filing | ❌ unattributed_proxy — no vendor identified | ✅ Account deactivated | ❌ Unknown | ✅ SRC-013 | ❌ No vendor attribution; unattributed_proxy limits analytical value |
| SHISH-002 | ✅ Abhishek Dhorelia verified as named claimant in notice | ⚠️ MarkScan / marcscan.in address; relationship to AiPlex unconfirmed | ✅ Account deactivated and restored | ✅ Restored | ✅ SRC-013; SRC-014 | 🔍 Confirm MarkScan ↔ AiPlex relationship via India MCA or LinkedIn |

---

### ПРOSTO ZHURNALISTIKA cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| PJ-001 | ❌ Unknown | ❌ unattributed_proxy | ✅ Account deactivated | ❌ Unknown | ✅ SRC-016; SRC-017 | ❌ No vendor; no appeal outcome. Two sources cover the removal only |
| PJ-002 | ❌ Unknown | ❌ unattributed_proxy | ✅ Channel terminated and restored | ✅ Restored 2025-08-06 | ✅ SRC-016 | ⚠️ Single source; vendor unattributed |

---

### RESPUBLIKA cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| RESP-001 | ❌ Not disclosed | ❌ unattributed_proxy | ✅ Page permanently lost (~41 000 followers) | ❌ Permanent loss | ✅ SRC-018 | ⚠️ Single source; permanent loss documented. Vendor gap is core research gap for entire Respublika campaign |
| RESP-002 | ⚠️ Giorgio Armani named but denied; no filing identity known | ❌ unattributed_proxy | ✅ 57 posts removed | ⚠️ Not appealed (editorial decision) | ✅ SRC-019; SRC-020 | 🔍 Obtain Armani denial statement as primary source (currently inferred) |
| RESP-003 | ⚠️ Same as RESP-002 | ❌ unattributed_proxy | ✅ Posts removed | ⚠️ Not appealed | ✅ SRC-019 | 🔍 Same; single source |
| RESP-004 | ✅ AiPlex named in notice; AIPLEX ID 40866 | ✅ claimed_affiliation + Google TR ID | ✅ 6 posts removed | ❌ Unknown | ✅ SRC-021 | 🔍 Attach Google TR snapshot; confirm Google TR 37% URL metric source |
| RESP-005 | ✅ AiPlex named | ✅ claimed_affiliation + Google TR ID | ✅ Wave of removals documented (21→61→358) | ❌ Unknown | ✅ SRC-022; SRC-021 | 🔍 Attach Google TR snapshot; confirm exact removal counts with editorial |
| RESP-006 | ❌ Not disclosed | ❌ unattributed_proxy | ✅ Seven block/removal events documented | ❌ Unknown | ✅ SRC-022 | ⚠️ Single source; no vendor. Temporal clustering with RESP-004/005 is circumstantial evidence of same campaign |

**Cluster priority (HIGH):** The RESP-001 permanent page loss is the most severe documented outcome in the dataset and currently rests on a single source. Vendor gap for RESP-001/002/003/006 is the largest open research question in the Kazakhstan cluster.

---

### LEGAL MEDIA CENTRE cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| LMC-001 | ⚠️ Najib Abdul Rahman Khalid named; identity not verified against registry | ❌ unattributed_proxy | ✅ Channel blocked and restored | ✅ Restored next day | ✅ SRC-023 | 🔍 Verify Khalid identity in open databases; single source |
| LMC-002 | ✅ AiPlex reported as claimant | ✅ claimed_affiliation + Google TR ID | ✅ Account deactivated | ❌ Unknown | ✅ SRC-024; SRC-025; SRC-021 | 🔍 Confirm restoration/current status with target |
| LMC-003 | ✅ AiPlex reported as claimant | ✅ claimed_affiliation + Google TR ID | ✅ Page blocked | ✅ Restored after ~1 month | ✅ SRC-024; SRC-025; SRC-026 | ✅ No blockers |

---

### AZATTYQ cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| AZATTYQ-001 | ❌ Unknown | ❌ unattributed_proxy | ✅ Account deactivated and restored | ✅ Restored | ✅ SRC-027; SRC-028 | ⚠️ No vendor; two sources confirm removal/restoration |
| AZATTYQ-002 | ❌ Unknown | ❌ unattributed_proxy | ✅ Second distinct blocking episode; restored | ✅ Restored | ✅ SRC-027; SRC-028 | ⚠️ Same |

**Cluster note:** Temporal proximity to RESP and LMC campaigns (all July 2026) is noted in case notes as circumstantial co-occurrence. Vendor remains unattributed pending further research.

---

### MONITORI cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| MON-001 | ✅ Ripu Singh / Aditya Singh — self-admitted; WhatsApp exchange documented | ✅ self_admitted_sub_contractor (novel attribution type) | ✅ Channel terminated and restored | ✅ Restored | ✅ SRC-029 | 🔍 Single source (SRC-029 is Monitori's own reporting); obtain independent corroboration of WhatsApp exchange |
| MON-002 | ❌ Claimant identity assessed fictitious; no real match | ❌ unattributed_proxy | ✅ Page removed and restored | ✅ Restored | ✅ SRC-029 | 🔍 Same single-source issue; ultimate client unknown |

**Cluster priority (HIGH):** MON-001 is analytically the richest case in the dataset (self-admission of sub-contractor role, price list). Single-source status (target's own reporting) is a publication risk. Priority: obtain independent journalist corroboration of the WhatsApp exchange.

---

### GAYLAN MEDIA cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| GAYLAN-001 | ✅ AiPlex named in notices and in parliamentary legal notice | ✅ claimed_affiliation + parliamentary notice (highest confidence in dataset) | ✅ Content removed | ❌ Unknown | ✅ SRC-030 | 🔍 Single source; obtain copy of MP Dr. Abdillahi Hashi Abib's legal notice as primary document; confirm current content status |

**Cluster priority:** GAYLAN-001 is the only case with a parliamentary accusation naming a specific vendor. Single-source status must be resolved before use in policy brief. Priority: obtain the legal notice document and a second independent source (e.g. CPJ or local Somali media report).

---

## Actors — Evidence Gap Matrix

| Actor ID | Name | Registration confirmed | Privileged access status | Outstanding gap |
|----------|------|------------------------|--------------------------|------------------|
| ACT-001 | AiPlex Software Pvt Ltd | ✅ India MCA U72200KA2003PTC032145 | ⚠️ claimed_but_unconfirmed_by_platform | 🔍 Attach current Google TR reporter page snapshot; confirm no EU establishment (Article 22 DSA) |
| ACT-002 | MarkScan Digital IP | ❌ No registration record | ❌ unknown | 🔍 Search India MCA for marcscan.in registrant; confirm or rule out AiPlex subsidiary relationship |
| ACT-003 | Eliminalia S.L. | ✅ Spain BORME B67704901 | ❌ unknown | ⚠️ Confirm current registration status (company may have been wound down post-2023 exposure) |
| ACT-004 | Ares Rights | ❌ Spain BORME record not obtained | ❌ unknown | ❌ HIGH: obtain primary registry entry |
| ACT-005 | Initiatrix Technologies | ❌ India MCA record not confirmed | ❌ unknown | ❌ HIGH: search MCA for exact company name |
| ACT-006 | Mogul Press | ❌ US state of incorporation unknown | ❌ unknown | 🔍 Search Delaware / Wyoming / Nevada SOS for Mogul Press |
| ACT-007 | Bytescare | ❌ India MCA record not confirmed | ❌ unknown | 🔍 Search India MCA |
| ACT-029 | Ripu Singh / Aditya Singh | ❌ Individual; no company registration | ❌ N/A | 🔍 Identify employing entity; confirm relationship to AiPlex or affiliate |

---

## Priority Research Queue

Ordered by impact on publication readiness:

1. **MON-001 second source** — WhatsApp exchange corroboration. Highest narrative value case.
2. **GAYLAN-001 legal notice document** — Parliamentary accusation; needed for policy brief.
3. **RESP-001 second source** — Permanent page loss; most severe outcome in dataset.
4. **AIPLEX-001 upgrade to Confirmed** — Only `Unverified` case; requires second source + account confirmation.
5. **ACT-004 (Ares Rights) registry record** — Needed before Ares Rights can be used as a confirmed vendor in outputs.
6. **ACT-005 (Initiatrix Technologies) registry record** — Same rationale.
7. **SHISH-002 MarkScan ↔ AiPlex link** — If confirmed, strengthens AiPlex attribution across Kazakhstan cluster.
8. **ELIM-008 vendor attribution upgrade** — Only Eliminalia case where vendor link is weak.
9. **Google TR snapshot archival** (RESP-004/005, LMC-002/003, GAYLAN-001) — Volatile evidence; archive immediately.

---

## Source Completeness

All source IDs referenced in `cases.csv` (SRC-001 through SRC-030) must have corresponding rows in `data/sources.csv`. Current status: **to be verified** against `data/sources.csv` in next audit sprint.
