## Evidence & Attack Simulation

The following lab scenarios were performed to validate detection logic.

---

# Phase 1 — SSH Brute Force (Implemented)

### Target Machine
- Ubuntu Linux VM

### Source
- Personal laptop or secondary VM

### Actions
- Attempt SSH login using an incorrect password
- Repeat 6–10 times
- Same username
- Same source IP
- Within 1–2 minutes

### Expected Evidence
- Multiple `Failed password` entries in `/var/log/auth.log`
- Same source IP
- Same username
- Closely spaced timestamps

### Detection Rule Triggered
- Detection Rule 1 — SSH Brute Force

---

# Phase 2 — Credential Spraying (Planned)

### Target Machine
- Ubuntu Linux VM

### Actions
- Create 3–5 user accounts
- Attempt SSH login once per user
- Same source IP
- Mostly failed attempts
- Within 5–10 minutes

### Expected Evidence
- Failed login attempts
- Multiple distinct usernames
- Same source IP

### Detection Rule
- Detection Rule 2 — Credential Spraying (Planned)

---

# Phase 3 — Success After Repeated Failures (Planned)

### Target Machine
- Ubuntu Linux VM

### Actions
- Perform several failed SSH login attempts from the same source IP
- Then perform a successful login
- Within 10–15 minutes

### Expected Evidence
- Multiple failed authentication events
- Followed by a successful login
- Same source IP

### Detection Rule
- Detection Rule 3 — Success After Failure (Planned)

