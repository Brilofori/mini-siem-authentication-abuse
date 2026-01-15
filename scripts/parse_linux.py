import re

LOG_FILE = r"logs\linux\linux_auth.log"

TIMESTAMP_PATTERN = re.compile(
    r'^(?P<timestamp>\S+)'
)

FAILED_PASS = re.compile(
    r'sshd\[(?P<pid>\d+)\]:\s+Failed password for\s+(?P<user>\S+)\s+from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
)

SUCCESS_PASS = re.compile(
    r'sshd\[(?P<pid>\d+)\]:\s+Accepted password for\s+(?P<user>\S+)\s+from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)'
)



