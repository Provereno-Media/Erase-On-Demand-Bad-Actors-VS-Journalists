# Contributing to Erase on Demand

Thank you for your interest in contributing to the **Erase on Demand** dataset and documentation. This project documents systemic abuse of platform moderation, notice-and-takedown, and copyright systems used to suppress independent journalism, media outlets, and civil society organizations.

We welcome contributions from investigative journalists, OSINT researchers, media lawyers, platform accountability advocates, and impacted newsrooms.

---

## Ways to Contribute

1. **Submit a New Case**: Propose an episode of takedown abuse against a media outlet or civil society organization.
2. **Provide Verifying Evidence**: Supply primary documentation (takedown notices, case IDs, headers, Lumen links, restoration notices) for existing cases marked `Unverified` or `Plausible`.
3. **Report Factual Errors / Corrections**: Notify us of inaccuracies in dates, claimants, URLs, or platform actions.
4. **Improve Data Infrastructure**: Contribute schema validation scripts, visualizers, or documentation improvements.

---

## Case Submission Guidelines

Before proposing a new case, verify that it meets the **Scope of Inclusion** defined in `codebook.md` and `README.md`:

### ✅ What Qualifies for `data/cases.csv`
- **Target**: An institutional media outlet, investigative newsroom, named media project, or press-freedom NGO (not private personal social media accounts of individuals).
- **Mechanism**: Abuse of platform enforcement procedures (DMCA/copyright takedowns, trademark claims, GDPR/RTBF notices, or hosting-level deplatforming).
- **Observable Platform Action**: Content removal, strike, demonetization, page/channel suspension, or deactivation; OR a documented filing in the Lumen Database whose outcome is under investigation.
- **Verifiable Evidence**: At least one primary document or independent published investigation.

### ❌ What Belongs to `data/comparative_cases.csv` or Context Only
- Incidents on Telegram (documented as narrative context only).
- Infrastructure-level cyberattacks (DDoS, account hijacking, password brute-forcing).
- SLAPP suits, defamation court filings, or physical surveillance without platform takedowns.
- Content takedowns targeting purely commercial entertainment or non-journalistic entities (e.g., music/movie piracy claims).
- Confirmed rejected notices where the platform took no restrictive action against the media.

---

## Submission Process

### Option A: Via GitHub Issues (Recommended for Public Leads)
1. Open a new issue using the **[Case Proposal]** or **[Evidence / Correction]** template.
2. Include:
   - Target name, platform, and country of origin.
   - Exact dates of notice and platform action.
   - Reported claimant name and claimed legal basis.
   - Public links (investigative reporting, Lumen notice URLs, public statements).
   - Expected confidence rating (`Confirmed`, `Plausible`, `Unverified`).

### Option B: Via Confidential Channels (For Sensitive Documents)
If your evidence contains unredacted email headers, non-public correspondence with platform support, or sensitive identity information:
- **Do NOT post unredacted personal data directly to GitHub.**
- Contact the research team securely via email: `tech-accountability@provereno.media` (PGP key available upon request) or through secure messaging.
- Submitted materials will be reviewed, redacted, and placed in the project's encrypted **Evidence Vault**, while only anonymized/public metadata will be committed to `cases.csv`.

---

## Coding Standards & Pull Requests

If submitting a Pull Request (PR) updating `data/cases.csv` or `data/sources.csv`:

1. **Follow the Schema**: Strictly adhere to the controlled vocabularies defined in `docs/codebook.md`.
2. **Assign IDs Consistently**:
   - `case_id`: Follow existing prefixes (`RESP-001`, `LMC-001`, `ELIM-001`).
   - `campaign_id`: Group related cross-platform episodes under a single campaign ID (`CMP-RESP-01`).
   - `source_ids`: Add all supporting citations to `data/sources.csv` first and cross-reference them by `source_id`.
3. **No Uncorroborated Allegations**: Clearly distinguish between the *reported claimant identity* and the *attributed underlying vendor/client*. Use `claimant_identity_verified = no` or `unknown` when impersonation is suspected.
4. **Validate Data**: Ensure the PR does not break `datapackage.json` validation.

---

## Code of Conduct

We are committed to maintaining a professional, collaborative, and evidence-driven research environment. All participants are expected to uphold rigorous factual accuracy, respect source confidentiality, and adhere to standard open-source collaboration ethics.
