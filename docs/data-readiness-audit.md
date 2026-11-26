# Data Readiness Audit

> **Historical snapshot.** This audit reflects the dataset as of 2026-10-14 (33 episodes). Later changes, including the v1.0.1 definition of `Confirmed` (which also covers a recorded researcher verification) and the corrections in v1.0.2 and v1.0.3, are listed in `CHANGELOG.md` and summarised under Known Limitations in `README.md`. Where this document and the data differ, `data/cases.csv` and `data/sources.csv` take precedence.

**Last updated:** 2026-10-14  
**Scope:** `data/cases.csv` (33 rows) and `data/actors.csv` (29 rows)  
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
| ARES-001 | ⚠️ Ares Rights self-identified in notices | ⚠️ claimed_affiliation only | ✅ Removed from Scribd and Dropbox, restored | ✅ Restored (EFF: counter-notice; CPJ: host switch) | ✅ SRC-001; SRC-040 | — |
| ARES-002 | ⚠️ Same as above | ⚠️ claimed_affiliation only | ⚠️ Removal reported by EFF and Chevron | ❌ Restoration not documented | ⚠️ SRC-001; SRC-041; SRC-042 (Chevron statement relayed) | 🔍 `Unverified`: Lumen notice or Wayback snapshot of youtube.com/texacoecuador needed |
| ARES-003 | ❌ Sender of this complaint not named by CPJ | ⚠️ unattributed_proxy (recoded 2026-11-26; CPJ lists Plan V among Ares Rights targets but not as sender of this complaint) | ⚠️ Removal reported by Plan V director; host unknown | ❌ Outcome unknown | ⚠️ SRC-040 | 🔍 `Unverified`: Lumen notice or Wayback snapshot of the Esmeraldas report needed |

**Cluster priority:** ✅ Ares Rights SL registry record obtained from BORME (2026-09-28). Remaining: fresh Registro Mercantil extract for current status. 2026-10-14: SRC-002 (a Qurium report on Eliminalia that does not mention Ares Rights) removed from ARES-001/002; SRC-001 (EFF, May 2014) removed from ARES-003, which it predates. ARES-002 and ARES-003 recoded `Unverified` pending Lumen or Wayback verification.

---

### AIPLEX cluster (AiPlex / ANN7)

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| AIPLEX-001 | ⚠️ AiPlex named in notices; identity not independently verified | ⚠️ claimed_affiliation (SRC-039 reports claims filed by AiPlex Software) | ✅ Video removals reported (TVwithThinus and other uploaders of ANN7 clips) | ⚠️ Partially restored or re-uploaded; extent not documented | ✅ SRC-003; SRC-039 | 🔍 Add a second public source that documents the removals (SRC-003 does not); confidence `Confirmed` |

**Cluster priority:** AIPLEX-001 is coded `Confirmed` (2026-09-30). Remaining: a second public source that documents the removals, and the extent of restoration.

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
| SHISH-001 | ⚠️ Purported Kazakh orgs denied filing | ❌ unattributed_proxy — no vendor identified | ✅ Account deactivated and permanently deleted | ❌ Permanent loss | ✅ SRC-013 | ❌ No vendor attribution; unattributed_proxy limits analytical value |
| SHISH-002 | ✅ Abhishek Dhoreliya verified as named claimant in notice | ⚠️ MarkScan / markscan.in address; relationship to AiPlex unconfirmed | ✅ Account deactivated and restored | ✅ Restored | ✅ SRC-013; SRC-014 | 🔍 Confirm MarkScan ↔ AiPlex relationship via India MCA or LinkedIn |

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
| RESP-001 | ❌ Not disclosed | ❌ unattributed_proxy | ✅ Page removed (~41 000 followers), later restored | ✅ Restored after RSF intervention (2026-11-24 update) | ✅ SRC-018; SRC-052; SRC-062 | ✅ Restoration confirmed by a Provereno researcher (SRC-062). Vendor gap is core research gap for entire Respublika campaign |
| RESP-002 | ⚠️ Giorgio Armani named but denied; no filing identity known | ❌ unattributed_proxy | ✅ 57 posts removed; restoration claimed (SRC-058, SRC-059), not confirmed with newsroom | ⚠️ Not appealed (editorial decision) | ✅ SRC-019; SRC-020; SRC-058; SRC-059 | 🔍 Obtain Armani denial statement as primary source (currently inferred) |
| RESP-003 | ⚠️ Same as RESP-002 | ❌ unattributed_proxy | ✅ Posts removed; restoration claimed (SRC-058, SRC-059), not confirmed with newsroom | ⚠️ Not appealed | ✅ SRC-019; SRC-052; SRC-058; SRC-059 | 🔍 Same; confirm restoration with newsroom |
| RESP-004 | ✅ AiPlex named in notice | ✅ claimed_affiliation | ✅ 6 posts removed | ❌ Unknown | ✅ SRC-020; SRC-021; SRC-031 (closed vault); SRC-038 | 🔍 No Google TR snapshot attached (`sender_volume_evidence` cites SRC-038); notices in the vault contain a MarkScan domain address |
| RESP-005 | ✅ AiPlex named | ✅ claimed_affiliation | ✅ Wave of removals documented (21→61→358) | ❌ Unknown | ✅ SRC-022; SRC-021; SRC-032 (closed vault); SRC-038 | 🔍 No Google TR snapshot attached; confirm exact removal counts with editorial; notices in the vault contain a MarkScan domain address |
| RESP-006 | ❌ Not disclosed | ❌ unattributed_proxy | ✅ Seven block/removal events documented | ⚠️ Partially restored | ✅ SRC-022; SRC-060; SRC-061 | ⚠️ Single source; no vendor. Temporal clustering with RESP-004/005 is circumstantial evidence of same campaign |

**Cluster priority (HIGH):** RESP-001 was recoded from permanent loss to restored (2026-11-24; researcher-confirmed, SRC-062). Vendor gap for RESP-001/002/003/006 is the largest open research question in the Kazakhstan cluster.

---

### LEGAL MEDIA CENTRE cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| LMC-001 | ⚠️ Najib Abdul Rahman Khalid (account name as quoted by the foundation); identity not verified | ❌ unattributed_proxy | ✅ Channel blocked and restored | ✅ Restored next day | ✅ SRC-023 | 🔍 Verify Khalid identity in open databases; single source |
| LMC-002 | ⚠️ AiPlex reported as claimant; attribution inferred from timing (SRC-033) | ⚠️ claimed_affiliation; no primary Meta notice | ✅ Account deactivated 16 Apr, restored after ~2 weeks | ✅ Restored (SRC-057) | ✅ SRC-024; SRC-025; SRC-021; SRC-033 (inferred); SRC-038; SRC-057 | 🔍 Obtain primary notice; Meta notice reportedly cited fraud and deception, not copyright — check `enforcement_basis` |
| LMC-003 | ⚠️ AiPlex reported as claimant; attribution inferred from timing (SRC-034) | ⚠️ claimed_affiliation; no primary Meta notice | ✅ Page blocked | ✅ Restored after ~1 month | ✅ SRC-024; SRC-025; SRC-026; SRC-034 (inferred); SRC-038 | ⚠️ AiPlex attribution inferred; no primary Meta notice |

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
| MON-001 | ✅ Ripu Singh (name in YouTube notice) — self-admitted; WhatsApp exchange documented | ✅ self_admitted_sub_contractor (novel attribution type) | ✅ Channel terminated and restored | ✅ Restored | ✅ SRC-029 | 🔍 Single source (SRC-029 is Monitori's own reporting); obtain independent corroboration of WhatsApp exchange |
| MON-002 | ❌ Claimant identity assessed fictitious; no real match | ❌ unattributed_proxy | ✅ Page removed and restored | ✅ Restored | ✅ SRC-029 | 🔍 Same single-source issue; ultimate client unknown |

**Cluster priority (HIGH):** MON-001 is analytically the richest case in the dataset (self-admission of sub-contractor role, price list). Single-source status (target's own reporting) is a publication risk. Priority: obtain independent journalist corroboration of the WhatsApp exchange.

---

### GAYLAN MEDIA cluster

| Case ID | Claimant identity | Vendor attribution | Platform action | Appeal outcome | Source count | Blocker |
|---------|------------------|--------------------|-----------------|----------------|--------------|---------|
| GAYLAN-001 | ✅ AiPlex named in notices and in parliamentary legal notice | ✅ claimed_affiliation + parliamentary notice (highest confidence in dataset) | ✅ Content removed | ❌ Unknown | ⚠️ SRC-030; SRC-035; SRC-036 (same public statement); SRC-037 | 🔍 Obtain copy of MP Dr. Abdillahi Hashi Abib's legal notice as primary document; SRC-035 currently links to the MP's statement, not the Meta notice; confirm current content status |

**Cluster priority:** GAYLAN-001 is the only case with a parliamentary accusation naming a specific vendor. Three of the four listed sources point to the same public statement; SRC-037 adds independent context on the wider wave of restrictions. Priority: obtain the legal notice document and an independent report of the takedown itself (e.g. CPJ or local Somali media report).

---

## Actors — Evidence Gap Matrix

| Actor ID | Name | Registration confirmed | Privileged access status | Outstanding gap |
|----------|------|------------------------|--------------------------|------------------|
| ACT-001 | AiPlex Software Pvt Ltd | ✅ India MCA U72200KA2003PTC032145 | ⚠️ claimed_but_unconfirmed_by_platform | 🔍 Attach current Google TR reporter page snapshot; confirm no EU establishment (Article 22 DSA) |
| ACT-002 | MarkScan Digital IP | ❌ No registration record | ❌ unknown | 🔍 Search India MCA for markscan.in registrant; confirm or rule out AiPlex subsidiary relationship |
| ACT-003 | Eliminalia S.L. | ✅ Spain BORME B67704901 | ❌ unknown | ⚠️ Confirm current registration status (company may have been wound down post-2023 exposure) |
| ACT-004 | Ares Rights SL | ✅ BORME primary: RM Barcelona hoja B-321497 (2010, 2012, 2013 notices); CIF B64106016 secondary only | ❌ unknown | ⚠️ LOW: fresh official extract for current status (2026-09-28) |
| ACT-005 | Initiatrix Technologies | ❌ India MCA record not confirmed | ❌ unknown | ❌ HIGH: search MCA for exact company name |
| ACT-006 | Mogul Press | ❌ US state of incorporation unknown | ❌ unknown | 🔍 Search Delaware / Wyoming / Nevada SOS for Mogul Press |
| ACT-007 | Bytescare | ❌ India MCA record not confirmed | ❌ unknown | 🔍 Search India MCA |
| ACT-029 | Ripu Singh (name in YouTube notice) | ❌ Individual; no company registration | ❌ N/A | 🔍 Identify employing entity; confirm relationship to AiPlex or affiliate |

---

## Priority Research Queue

Ordered by impact on publication readiness:

1. **MON-001 second source** — WhatsApp exchange corroboration. Highest narrative value case.
2. **GAYLAN-001 legal notice document** — Parliamentary accusation; needed for policy brief.
3. **AIPLEX-001 second public source** — Now `Confirmed`; add a second public source that documents the removals.
4. **ACT-004 (Ares Rights) registry record** — Needed before Ares Rights can be used as a confirmed vendor in outputs.
5. **ACT-005 (Initiatrix Technologies) registry record** — Same rationale.
6. **SHISH-002 MarkScan ↔ AiPlex link** — If confirmed, strengthens AiPlex attribution across Kazakhstan cluster.
7. **ELIM-008 vendor attribution upgrade** — Only Eliminalia case where vendor link is weak.
8. **Google TR snapshot archival** (RESP-004/005, LMC-002/003, GAYLAN-001) — Not attached; `sender_volume_evidence` now cites public articles instead. Volatile evidence; archive immediately.
9. **SRC-022 link** — Title refers to the April 2026 wave counts and Instagram statistics, but the URL points to post 14258 (8 March 2026, 'Giorgio Armani' removals). Find the correct April post(s) and fix the URL; check SRC-033 (same URL) as well.
10. **LEMONDE-001 archive** — Lumen notice 40471185 checked by a researcher (SRC-064, 2026-11-25); add a Wayback snapshot to `archive_url` and confirm the claimed Frontier Times "original" URL (`abuse_mechanism = backdated_article`).
11. **Malta (CTX-MT-001)** — Retrieve the Lumen notices behind Google's removal messages for Maltese news sites and blogs (search terms used by EDMO/MedDMO: "ram tumuluri", "vitals global healthcare") to identify target outlets, dates and claimants; episodes meeting §3 criteria move to `cases.csv`.

---

## Source Completeness

All source IDs referenced in `cases.csv` (SRC-001 through SRC-042) have corresponding rows in `data/sources.csv` (checked 2026-10-14; also enforced by `scripts/validate.py`).
