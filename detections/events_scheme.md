Normalized Authentication Event Schema
=====================================

Each authentication event from any platform is normalized into the following structure.

Fields
------

timestamp
- UTC timestamp of the event
- Type: datetime

platform
- Originating operating system
- Values: linux | windows

host
- Hostname of the system where the event occurred
- Example: ubuntu-srv01, win10-client

username
- Account involved in the authentication attempt
- May be "unknown" if user does not exist

source_ip
- IP address where the authentication attempt originated
- Null if not available

event_type
- Category of event
- Value: authentication

outcome
- Result of the authentication attempt
- Values: success | failure

raw_event_id
- Native identifier from source logs
- Examples:
  - linux: sshd
  - windows: 4624, 4625
