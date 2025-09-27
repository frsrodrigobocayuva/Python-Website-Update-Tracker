# Python-Website-Update-Tracker

A lightweight, single-purpose Python script that periodically checks a Google News RSS feed, detects newly published items, and sends an email alert when a new title appears.
**This repository and its code were created strictly as a portfolio piece to demonstrate skills for future job applications — it is not intended for production use.**

---

# Project summary

**Python-Website-Update-Tracker** is a compact, intentionally simple automation that shows practical ability in:

* Python scripting and small-scale program structure
* Reading and parsing external feeds (RSS)
* Basic persistence (text file)
* Sending email via SMTP
* Thinking about scheduling and automation (Windows Task Scheduler used in the project)

---

# What’s included (repository-specific)

* `main.py` — the single, self-contained script that implements the project’s core behavior:

  * reads a Google News RSS URL (hard-coded by default),
  * extracts the most recent entry title,
  * compares it to the stored title in `previousTitles.txt`,
  * sends an email when a change is detected,
  * updates `previousTitles.txt` after a successful notification. 

* `previousTitles.txt` — a runtime file used to persist the last-seen title (created and updated by the script during execution).

* `requirements.txt` — a minimal list of runtime packages used by the script.

* `.gitignore` — standard git ignore rules to keep virtual environments, credentials, compiled files and other local artifacts out of source control. 

* `run_monitor.bat` — a simple Windows batch file included to start the monitor locally or to be referenced by a Task Scheduler action for demo purposes.

**Note:** This repository was created by me as a focused job-application portfolio item. The code and configuration are intentionally minimal and tailored for demonstration — not intended or vetted for production use.

---

# How it works (high-level flow)

1. The script parses the RSS feed (Google News RSS).
2. It reads the title from the feed.
3. It compares that title to the content of `previousTitles.txt`.
4. If the title is different, it sends an email alert using configured SMTP credentials.
5. After a successful send, it writes the new title to `previousTitles.txt`.

---

# Important disclaimer — portfolio use only

**Do not use this code in production or for real automation.**
This repository was created solely as a portfolio piece to demonstrate skills to recruiters and hiring managers. It **has not** been code-reviewed, security-audited, or tested for real-world operation.

Key reasons you should not run this as a production service:

* **Not reviewed:** The code has not undergone peer review or a formal audit. It may contain bugs, insecure practices, or logic flaws.
* **No security hardening:** There was no attempt to make the project meet security standards. Secrets handling, authentication, and transport security are implemented only for simplicity — not for safety.
* **Untested:** The script was not subjected to systematic unit, integration, or load testing. Behaviour under failure conditions is unknown.
* **Not intended for real use:** The design decisions prioritize clarity and teachability for interviews rather than resilience, scalability, or reliability.
* **Environment limitations:** Scheduling guidance in this repo targets Windows Task Scheduler only; there is no cron/Linux support or deployment automation.
