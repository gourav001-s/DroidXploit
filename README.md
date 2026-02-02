# DroidXploit Framework

DroidXploit is an all-in-one **Android security assessment framework** designed for
**rooted Android emulators**.  
It provides a clean, modular, menu-driven CLI interface for Android application
enumeration, runtime analysis, and exploitation research.

> ⚠️ For educational purposes and authorized testing only.

---

<img width="597" height="566" alt="Screenshot 2026-02-02 182656" src="https://github.com/user-attachments/assets/5cfbaa3b-019d-45c2-ba79-f9ea36626148" />


## ✨ Key Features

- Device & OS enumeration
- Installed application discovery
- Private app data dumping
- Token & secret discovery
- SQLite database intelligence
- SSL pinning bypass (Frida-assisted)
- Runtime memory inspection helpers
- Root & emulator detection checks
- Full app assessment attack chain
- Markdown report generation
- Clean and professional CLI UI

---

## 🧠 Design Philosophy

DroidXploit is **not** a one-click hacking tool.

The framework focuses on:
- Transparency over blind automation
- Analyst-controlled exploitation
- Methodology-driven Android assessments
- Real-world bug bounty and research relevance

Each module assists the tester instead of hiding what happens internally.

---

## 🛠 Requirements

- Linux (Kali Linux recommended)
- Python 3.8+
- Android Debug Bridge (ADB)
- Rooted Android emulator
- Frida (for runtime analysis and SSL pinning bypass)

---

## 🚀 Installation

```bash
git clone https://github.com/gourav001-s/droidxploit.git
cd droidxploit
python3 adb_osint.py

```
Ensure:
Emulator is running

Root access is available

adb and frida are in your PATH

## 📋 Usage
Run the framework:

python3 androidxploit.py

Select modules using the indexed menu:

[1] Device Enumeration

[11] App Intelligence

[16] Full App Assessment

## 🔗 Example Workflow

Run Pre-Flight Check

Enumerate device and installed apps

Perform App Intelligence scanning

Dump private app data

Analyze SQLite databases

Hunt for tokens and secrets

Perform runtime analysis using Frida

Generate a security assessment report

## 📁 Output
Application data dumps stored locally

Console output for findings

Report generated as:

androidxploit_report.md

## ⚠️ Legal Disclaimer
This framework is intended for educational purposes and authorized security testing only.

You must:

Own the device and application being tested, or

Have explicit permission from the owner

The author assumes no responsibility for misuse.

## 👤 Author
Gourav (RaVX)

GitHub: https://github.com/gourav001-s

## ⭐ Contributions
Contributions and improvements are welcome.

Please ensure:

Ethical usage

Clean code

Transparent modules

Pull requests promoting illegal activity will not be accepted.
