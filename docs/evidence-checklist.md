# Evidence Checklist for Case Submissions

This checklist defines the minimum necessary documentation required to evaluate, code, and admit an attack episode into `data/cases.csv` or `data/comparative_cases.csv`. 

Researchers and contributing investigative newsrooms should use this checklist when assembling case documentation.

---

## 1. Mandatory Core Evidence (Minimum Threshold for Admission)

A candidate case **must satisfy all 5 requirements** below to be admitted into `data/cases.csv`:

- [ ] **1. Identifiable Institutional Target**
  - Name of the media outlet, publication, investigative project, or civil society organization.
  - URL of the targeted website, verified social media handle, YouTube channel, or hosting account.
  - Confirmation that the target operates as a media or civil society entity (not an unrelated commercial business or private personal profile).

- [ ] **2. Documented Platform Enforcement Action**
  - Date and time the restriction, strike, or removal occurred.
  - Specific platform involved (Meta Facebook, Meta Instagram, YouTube, Google Search, hosting provider, domain registrar).
  - Concrete platform action observed (content removal, channel deactivation, page unpublished, account locked, strike issued).
  - *Exception:* For Google Search delisting, a verifiable Lumen Database notice record is acceptable even if search engine action remains `unknown`.

- [ ] **3. Primary Notice or Notification Text**
  - Copy or screenshot of the platform notification sent to the account owner.
  - Notice text stating the reason for removal (copyright infringement, trademark infringement, terms violation).
  - Case, Reference, Strike, or Report ID assigned by the platform (e.g., Meta Report ID, YouTube Strike ID).

- [ ] **4. Complainant / Claimant Information (As Reported)**
  - Name of the individual or organization submitting the claim as reported by the platform notification.
  - Sender email address or contact point provided by the platform (if disclosed).
  - Description of the copyrighted work or trademark allegedly infringed.

- [ ] **5. Independent Source Corroboration**
  - At least one independent public source (investigative report, official statement, Lumen Database record, regulator filing) corroborating the event.

---

## 2. Technical & Forensic Corroboration (Required for Confirmed Status)

To elevate a case from `Unverified` or `Plausible` to `Confirmed`, collect as many of the following technical artifacts as possible:

- [ ] **Raw Notification Headers:** Original `.eml` or full header export of the platform notice email (verifying SPF, DKIM, and sending server authenticity).
- [ ] **Original Content Archiving:** Permanent archival permalinks (Wayback Machine or Archive.today) of the targeted investigative article, video, or social post *prior* to the takedown.
- [ ] **Infringing / Cloned URL Inspection (for backdated article schemes):**
  - Complete URL of the fake or mirror domain claiming original authorship.
  - WHOIS / RDAP query capture proving domain registration date postdates the original investigation.
  - Wayback Machine check showing the fake URL did not exist prior to the target publication date.
  - Local snapshot/screenshot of the cloned article showing falsified publication timestamps and author names.
- [ ] **Lumen Database Notice ID:** Direct URL or API record identifier for the notice in the Lumen Database (lumendatabase.org).
- [ ] **Network & Domain Infrastructure:** Hosting IP, ASN, nameserver history, and DNS records of the claimant domain (if hosted on disposable infrastructure).

---

## 3. Appeal & Remediation Tracking

To ensure accurate coding of `appeal_outcome` and `date_end`:

- [ ] **Counter-Notification Documentation:** Date, text, and statutory basis of formal DMCA counter-notice or platform appeal filed by the newsroom.
- [ ] **Platform Response:** Formal email or notification from the platform accepting, rejecting, or ignoring the appeal.
- [ ] **Third-Party Mediation Details:** Documentation of interventions by press freedom organizations (e.g., Access Now Digital Security Helpline, CPJ, RSF, Qurium Media Foundation).
- [ ] **Restoration Timestamp:** Exact date when access to the content, page, or channel was fully reinstated.
- [ ] **Completeness of Restoration:** Verification whether all content, view counts, comments, and subscriber metrics were restored or if residual penalties (e.g., shadowbans, ad restrictions) remained.

---

## 4. Submission Packaging Protocol

When transferring case files to the research repository:
1. **Sanitization:** Ensure private home addresses, phone numbers, and non-work personal email addresses of newsroom staff are redacted from public uploads.
2. **File Naming Convention:** Name supporting files using the case identifier:
   - `[CASE_ID]_notice_redacted.png`
   - `[CASE_ID]_lumen_record.pdf`
   - `[CASE_ID]_appeal_timeline.txt`
3. **Vault Deposit:** Deposit raw, unredacted email files (`.eml`), server logs, and correspondence into the encrypted research vault and record the corresponding `vault_reference` ID in `data/sources.csv`.
