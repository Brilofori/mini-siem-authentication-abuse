import re
from collections import defaultdict
from datetime import datetime


LOG_FILE = r"logs\linux\linux_auth.log"

TIMESTAMP_PATTERN = re.compile(
    r'^(?P<timestamp>\S+)'
)

FAILED_PASS = re.compile(
    r'sshd\[\d+\]:\s+Failed password for(?: invalid user)?\s+(?P<user>\S+)'
    r'\s+from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
)

SUCCESS_PASS = re.compile(
    r'sshd\[\d+\]:\s+Accepted password for\s+(?P<user>\S+)'
    r'\s+from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
)

def parse_linux_auth_log():
    events = []

    with open(LOG_FILE, "r", encoding="utf-8") as linux_log:
        for line in linux_log:
            line = line.strip()

            # Extract timestamp (best-effort)
            ts_match = TIMESTAMP_PATTERN.search(line)
            timestamp = ts_match.group("timestamp") if ts_match else None

            failed = FAILED_PASS.search(line)
            success = SUCCESS_PASS.search(line)

            if failed:
                events.append({
                    "timestamp": timestamp,
                    "platform": "linux",
                    "host": "ubuntu-srv01",
                    "username": failed.group("user"),
                    "source_ip": failed.group("ip"),
                    "event_type": "authentication",
                    "outcome": "failure",
                    "raw_event_id": "sshd"
                })

            elif success:
                events.append({
                    "timestamp": timestamp,
                    "platform": "linux",
                    "host": "ubuntu-srv01",
                    "username": success.group("user"),
                    "source_ip": success.group("ip"),
                    "event_type": "authentication",
                    "outcome": "success",
                    "raw_event_id": "sshd"
                })

    return events

#SOURCE GROUP BY IP 

def group_events_by_ip(events):
    grouped = defaultdict(list)

    for event in events:
        if event["source_ip"]:
            grouped[event["source_ip"]].append(event)

    return grouped

def detect_ssh_bruteforce(grouped_events, threshold = 5, window_minutes = 5):
    pass





#THE MAIN BLOCK EXECUTION 
if __name__ == "__main__":
    parsed_events = parse_linux_auth_log()
    print(f"Parsed {len(parsed_events)} Linux authentication events")

    for event in parsed_events[:5]:
        print(event)