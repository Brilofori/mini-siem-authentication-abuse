##Description 

Detect repeated failed SSH logins from the same source IP

##Logic
 
- More than 5 failed login attempts
- From the same source IP
- Within 5 minutes 
- Against any user  
 
###Why?
- It indicates likely automated password guessing against the linux system

##Description

Detect login attempts where a single source tries multiple usernames.

##Logic

- Same source IP

- Attempts against 3 or more different users

- Within 10 minutes

- Mostly failed logins

##Why?
- Indicates credential spraying, often used to avoid lockouts.


Detection Rule 3 — Success After Failure (Cross-Platform)

##Description
Detect a successful login following multiple failures from the same source.

##Logic

- ≥3 failed logins from a source IP

- Followed by a successful login

- On Linux or Windows

- Within 15 minutes

##Why?
Strong signal of compromised credentials.
