# Mini-SIEM: Linux SSH Brute-Force Detection Engine

## Overview

This project implements a detection-focused Mini-SIEM designed to identify SSH authentication abuse on Linux systems.

Rather than relying on commercial SIEM platforms, this project focuses on understanding how raw system logs can be parsed, normalized, and correlated to detect attacker behavior.

The goal is to understand detection engineering fundamentals — not just use existing tools.

---

## Aim

This project addresses:

- Parsing raw Linux authentication logs (`auth.log`)
- Normalizing SSH authentication events into structured data
- Correlating failed login attempts by source IP
- Detecting brute-force authentication patterns using time-based logic
- Producing explainable security alerts

---

## What This Project Does

- Ingests Linux SSH authentication logs
- Extracts timestamps, usernames, and source IPs using regex
- Groups authentication events by source IP
- Applies sliding time-window correlation
- Detects repeated failed login attempts within a defined threshold
- Generates structured brute-force alerts

---

## Detection Logic

The detection engine identifies brute-force behavior by:

1. Filtering failed SSH login attempts
2. Sorting events by timestamp
3. Applying a configurable time window (default: 5 minutes)
4. Triggering an alert when failures exceed a defined threshold (default: 5 attempts)

This approach simulates how correlation rules operate inside enterprise SIEM platforms.

---

## Lab Environment

- **Personal Laptop** – Detection engine and log analysis
- **Ubuntu VM** – SSH authentication log source
- Failed authentication attempts were intentionally generated to simulate brute-force behavior.

---

## Project Status

Linux SSH brute-force detection fully implemented.

### Future Improvements

- Windows Security Event Log ingestion
- Cross-platform authentication correlation
- Additional authentication abuse patterns
