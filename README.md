# Mini-SIEM: Cross-Platform Authentication Abuse Detection

## Overview
This project implements a lightweight, detection-focused Mini-SIEM designed to identify credential abuse by correlating authentication events across Linux and Windows systems.

Rather than relying on commercial SIEM platforms or dashboards, this project focuses on understanding how raw system logs can be used to reconstruct attacker behavior and make defensible security decisions.


## Problem  to address
Modern environments generate authentication logs across many systems, but no single host provides enough context to detect credential abuse on its own.

This project addresses that gap by:
- Normalizing authentication events from different operating systems
- Correlating related events across systems
- Detecting suspicious authentication patterns indicative of credential abuse


## What This Project Does
- Ingests Linux SSH authentication logs (`auth.log`)
- Ingests Windows Security Event Logs (Event IDs 4624 and 4625)
- Normalizes events into a common schema
- Correlates authentication activity across systems
- Detects credential abuse patterns using custom logic
- Produces explainable security alerts


## Machines Involved
- **Personal Laptop**: Log ingestion, correlation, and detection engine
- **Linux VM (Ubuntu)**: SSH authentication log source
- **Windows 10 VM**: Windows Security authentication log source



## Detection Focus
This project is detection-driven and prioritizes behavior over individual events.

Planned detections include:
- SSH brute-force attempts
- Password spraying activity
- Successful authentication following repeated failures
- Cross-system authentication abuse
---

## Project Status
Initial project structure and documentation complete. Detection logic and log correlation under development.

