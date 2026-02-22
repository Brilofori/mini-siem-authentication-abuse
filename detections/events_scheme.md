## Normalized Authentication Event Schema

All parsed SSH authentication events are normalized into a consistent internal structure.

The schema is designed to be platform-agnostic, allowing future support for additional authentication sources (e.g., Windows Security logs).

---

### Fields

**timestamp**
- UTC timestamp of the event  
- Type: `datetime`

**platform**
- Originating operating system  
- Current value: `linux`

**host**
- Hostname of the system where the event occurred  
- Example: `ubuntu-srv01`

**username**
- Account involved in the authentication attempt  
- May be `"invalid user"` if the account does not exist

**source_ip**
- IP address where the authentication attempt originated

**event_type**
- Category of event  
- Value: `authentication`

**outcome**
- Result of the authentication attempt  
- Values: `success` | `failure`

**raw_event_id**
- Native identifier from source logs  
- Example: `sshd`

