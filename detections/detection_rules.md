## Detection Rules

---

### Detection Rule 1 — SSH Brute-Force Attempt

#### Description
Detect repeated failed SSH login attempts from the same source IP address.

#### Logic
- More than 5 failed login attempts
- From the same source IP
- Within 5 minutes
- Against any username

#### Why?
A high number of failed attempts in a short time window strongly indicates automated password guessing against the Linux system.

---

### Detection Rule 2 — Credential Spraying (SSH)

#### Description
Detect login attempts where a single source IP tries multiple usernames.

#### Logic
- Same source IP
- Attempts against 3 or more different usernames
- Within 10 minutes
- Majority of attempts are failed logins

#### Why?
Credential spraying attempts multiple accounts with limited guesses per account to avoid lockouts and detection thresholds.

---

### Detection Rule 3 — Success After Repeated Failures

#### Description
Detect a successful SSH login following multiple failed attempts from the same source IP.

#### Logic
- 3 or more failed login attempts from a source IP
- Followed by a successful login
- Within 15 minutes

#### Why?
A successful login after multiple failures may indicate compromised credentials.