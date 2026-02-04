import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = r"logs\linux\linux_auth.log"

###regex 
TIMESTAMP_PATTERN = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})'
)
FAILED_PASS = re.compile(
    r'sshd\[\d+\]:\s+Failed password for(?: invalid user)?\s+(?P<user>\S+)'
    r'\s+from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
)
SUCCESS_PASS = re.compile(
    r'sshd\[\d+\]:\s+Accepted password for\s+(?P<user>\S+)'
    r'\s+from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
)
####

###parse the timestamp 
def parse_timestamp(ts_str):
    return datetime.fromisoformat(ts_str)

def parse_linux_auth_log():
    events = []

    with open(LOG_FILE, "r", encoding="utf-8") as linux_log:
        for line in linux_log:
            line = line.strip()

            # Extract timestamp 
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

def group_IP_to_event(events):
    grouped = defaultdict()
# information being extracted: the source ip and the line of log matching it 
    for event in events:
        if ['source_ip'] in event:
            grouped[event['source_ip']].append(event)
    
    return grouped


def detect_ssh_bruteforce(grouped_events, threshold = 5, window_minutes = 5):
   """
   Docstring for detect_ssh_bruteforce
   
   :param grouped_events: Description
   :param threshold: Description
   :param window_minutes: Description

        timestamp:  "platform": "linux",
                    "host": "ubuntu-srv01",
                    "username": success.group("user"),
                    "source_ip": success.group("ip"),
                    "event_type": "authentication",
                    "outcome": "success",
                    "raw_event_id": "sshd"
   """
    #lets extract
    #timestamp, source ip, how many times an alerts was attributed to an event,
    empty = []
    for key1, value1 in grouped_events.items():
        if value1['outcome'] == 'failure':
            empty.append(value1)


    for            
           
   



    output = {
        'alert type':'brute force',
        'source ip':{source_IP},
        'failed attempts':{failed_attempts},
        'first seen':{first_seen},
        'last seen':{last_seen}
    }

        
        
  
        




if __name__ == '__main__':
    events = parse_linux_auth_log(
    )
    print(f'[+] Parsed {len(events)} Linux authentication events')
    
    grouped = group_IP_to_event(events)
