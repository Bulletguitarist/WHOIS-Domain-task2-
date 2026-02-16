# WHOIS Domain Intelligence Tool

## 📌 Overview

This project is a Python-based WHOIS domain information checker built for OSINT and cybersecurity analysis purposes.

It fetches domain metadata such as registrar, creation date, expiration date, and DNS information, while handling edge cases like invalid or protected domains.

The results are stored locally in structured TXT and CSV formats for further analysis.

---

## 🎯 Objectives

- Automate domain WHOIS lookup
- Normalize inconsistent WHOIS date formats
- Handle protected or invalid domains gracefully
- Store structured domain intelligence locally
- Support phishing detection research workflows

---

## 🚀 Features

- Accepts user input for any domain
- Fetches WHOIS metadata using `python-whois`
- Cleans and formats date fields
- Handles errors without crashing
- Exports results to:
  - TXT file (per domain)
  - CSV file (aggregated)

---

## 🛠 Technologies Used

- Python 3.x
- python-whois
- csv module
- datetime module
- os module

---

## 📂 Project Structure

WHOIS Domai(task2/
│
├── .gitignore
├── whoischecker.py
└── README.md

---

## ⚙️ Installation

Install dependencies:
pip install python-whois

---

## ▶️ How to Run

Command- python whoischecker.py


Enter a domain name when prompted:
ex:- google.com

---

## 📊 Example Output

Domain: google.com
Registrar: MarkMonitor, Inc.
Creation Date: 1997-09-15
Expiry Date: 2028-09-14
Name Servers: NS1.GOOGLE.COM, NS2.GOOGLE.COM
---

## 🛡 Cybersecurity Use Case

This tool can be used for:

- Phishing domain investigation
- Domain age analysis
- OSINT research
- Suspicious TLD detection workflows
- SOC-level domain enrichment

---

## 📈 Possible Improvements

- Domain age risk scoring
- Bulk domain scanning
- JSON export support
- CLI argument parsing
- API integration


