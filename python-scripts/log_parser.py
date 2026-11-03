"""Local log analyzer - simulation / local test version.

Scans a log file for hardware and driver diagnostic keywords.
Default path is /var/log/messages on Rocky Linux / CentOS.
For testing, pass a sample log file path as the first argument.
Example: python3 log_parser.py sample_messages.log
"""
import sys

TARGET_FLAGS = ["hardware error", "mce", "pcie fault", "link down", "drive degraded"]


def scan_local_system_logs(log_path="/var/log/messages"):
    print(f"--- Initiating Diagnostic Analysis Scan on: {log_path} ---")
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as open_file:
            for line in open_file:
                if any(flag in line.lower() for flag in TARGET_FLAGS):
                    print(f"[ALERT MATCH]: {line.strip()}")
    except FileNotFoundError:
        print(f"[ERROR] Target path could not be located at: {log_path}")


if __name__ == "__main__":
    scan_local_system_logs(sys.argv[1] if len(sys.argv) > 1 else "/var/log/messages")
