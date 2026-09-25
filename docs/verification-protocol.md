# Verification Protocol

This document defines the verification standards, evidence hierarchies, attribution criteria, and cross-validation procedures for all entries and claims in the "Erase on Demand" dataset.

---

## 1. Core Principles

1. **Strict separation of claim tiers:** A verified platform action (e.g., post removal or account suspension) does not automatically verify the identity of the complainant, their claimed affiliation, or the underlying motive. Every distinct claim within a case must be evaluated independently.
2. **Fact over assumption:** Platforms frequently accept takedown notices from unverified or spoofed identities. No entity is identified as a confirmed perpetrator without direct forensic, institutional, or documentary corroboration.
3. **No legal accusations:** The project documents observable facts, platform behaviors, and evidentiary thresholds. It does not issue formal judicial findings or criminal accusations.
4. **Preservation of primary evidence:** Public summaries and secondary press reports are insufficient on their own for attributing malice or identifying systematic platform failure. Primary documents (notices, server logs, registry extracts) must be captured and preserved.

---

## 2. Three-Level Confidence Scale

Every case in `data/cases.csv` carries an overall `confidence` rating, and all analytical claims within case summaries must conform to these thresholds:

| Confidence Level | Definition | Minimum Evidentiary Requirement |
|---|---|---|
| **Confirmed** | Factual occurrence is verified beyond reasonable doubt. | Corroborated by **at least two independent, reliable sources** (e.g., platform notice + newsroom corroboration; Lumen entry + target domain verification; corporate registry extract + official court record). |
| **Unverified** | Factual occurrence is documented but relies on a single source. | Single direct source (e.g., unilateral public statement by affected newsroom without published notice; single uncorroborated media report; unconfirmed notice submission). |
| **Plausible** | Coherent, logical explanation consistent with established behavioral patterns, but lacks conclusive direct evidence. | Pattern-based attribution (e.g., notice mimics known vendor templates or IP addresses, but lacks cryptographic signatures, raw email headers, or explicit corporate attribution). |

---

## 3. Evidence Hierarchy

Evidence gathered during investigations is prioritized according to the following hierarchy:

```
Tier 1: Primary Platform & Technical Artifacts (Highest Authority)
  ├── Raw email notifications with full headers (DKIM, SPF, IP provenance)
  ├── Official platform case IDs, strike notices, and dashboard screenshots
  ├── Lumen Database submission notices (verified via Lumen API)
  ├── Official corporate registry filings (MCA India, UK Companies House, Dutch KvK, etc.)
  └── Historical DNS, WHOIS/RDAP records, and Wayback Machine / Archive.today snapshots

Tier 2: Direct Institutional Statements & Corroborated Reporting
  ├── Direct witness documentation from targeted newsrooms and legal teams
  ├── Technical forensic investigation reports (Qurium Media Foundation, Citizen Lab)
  ├── In-depth cross-border journalistic investigations (OCCRP, Forbidden Stories, consortiums)
  └── Official statements or admissions from platform representatives or regulatory bodies

Tier 3: Secondary Coverage & Unilateral Claims (Context Only)
  ├── Single-outlet news reporting without primary artifact citations
  ├── Editorial op-eds or public social media commentary
  └── Unverified whistleblower tips or anonymous submissions
```

---

## 4. Vendor Attribution Standard

Attributing a takedown notice to a commercial reputation-scrubbing firm, copyright-enforcement contractor, or state proxy requires meeting one of four explicit categories in `codebook.md`:

### 4.1 `confirmed`
Requires at least one of the following:
- Cryptographically verified email headers (DKIM/SPF) originating from the vendor's authenticated corporate domain.
- Official admission by the vendor, client, or platform representative.
- Direct identification in judicial, arbitral, or regulatory enforcement proceedings.
- Verifiable corporate registration documents linking the complainant identity directly to the operational entity.

### 4.2 `claimed_affiliation`
- The complainant explicitly named a recognized vendor (e.g., MarkScan, AiPlex, Ares Rights) or entered their brand/domain in a web form.
- *Caveat:* Third-party impersonation or pretexting cannot be eliminated without Tier 1 technical proof. Such cases must remain classified as `claimed_affiliation` until header verification or vendor confirmation is obtained.

### 4.3 `technical_forensic_attribution`
- Documented technical overlap established through forensic investigation: shared infrastructure, identical backdated-CMS templates, unique email address reuse patterns across Lumen notices, or forensic document metadata (e.g., author metadata in submitted PDF evidence).

### 4.4 `unattributed_proxy`
- Notices submitted via disposable free webmail providers (e.g., `@gmail.com`, `@proton.me`), fabricated shell company names, or generic legal personas where no technical link to an established vendor can be verified.

---

## 5. Backdated Article Verification Protocol

To verify claims of the "backdated article" mechanism (cloning an investigative article to a throwaway site, falsifying the publication date, and filing a DMCA takedown against the original publisher):

1. **Original Publication Date:** Verify timestamp of original article via Wayback Machine, RSS feed history, and publisher CMS database records.
2. **Mirror Domain Registration Date:** Query WHOIS/RDAP for domain registration date of the complainant site. If domain was registered *after* the original article was published, the backdating claim is verified.
3. **First Archive/Index Date:** Check Wayback Machine and search engine cache history for the earliest appearance of the cloned URL.
4. **Content Comparison:** Perform semantic and verbatim diff analysis to confirm the content was copied from the investigative report.
5. **Notice Correlation:** Locate corresponding takedown notice in Lumen Database linking the cloned URL as "original work" and the target newsroom as "infringing URL."

---

## 6. Data Sanitization & Personal Data Protection

To comply with applicable privacy standards (including GDPR principles) and prevent doxxing:
1. **Redaction of Non-Public Individuals:** Private email addresses, personal phone numbers, and physical residential addresses appearing in takedown notices must be redacted from all public repository files (`data/cases.csv`, `case-notes/`).
2. **Corporate & Public Identities:** Corporate registered offices, corporate domain names, and named corporate directors/representatives acting in their official commercial capacities are retained as public record.
3. **Closed Evidence Vault:** Unredacted copies of emails, notices, and raw server logs are deposited in an encrypted, access-controlled vault for academic and regulatory audit (referenced by `vault_reference` in `data/sources.csv`).
