Phase 1 — SSH Brute Force (Linux)
# Target Machine
- Linux VM


## Source
- Personal laptop (or Windows VM)


## Actions

- Attempt SSH login with an incorrect password
- Repeat 6–10 times
- Use the same username
- Same source IP
- Short time window (1–2 minutes)


## Expected Evidence

- Multiple Failed password entries in /var/log/auth.log
- Same IP
- Same user
- Tight timestamps

## Detection Rule Triggered
- Detection Rule 1 — SSH Brute Force



# Phase 2 — Password Spraying
#3 Target Machine
- Linux VM or Windows VM


## Actions

- Create 3–5 users
- Attempt login once per user
- Same source IP
- All or mostly failures
- Within 5–10 minutes


## Expected Evidence

- Failed login attempts
- Multiple usernames
- Same source IP


## Detection Rule Triggered

- Detection Rule 2 — Password Spraying



# Phase 3 — Success After Failure (Cross-Platform)

## Target Machines

- Linux VM and Windows VM


## Actions

- Perform several failed logins from same source
- Then perform a successful login
- Within 10–15 minutes
- Same source IP


## Expected Evidence
- Failed auth events
- Followed by success
- Across different systems


## Detection Rule Triggered
- Detection Rule 3 — Success After Failure

