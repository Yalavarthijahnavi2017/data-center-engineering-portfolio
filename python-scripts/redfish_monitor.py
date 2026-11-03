"""Redfish emulator telemetry parser - SIMULATION ONLY.

Reads a local mock JSON file (mock_thermal.json) by default, so it can be
tested without a real server, a real emulator, or any credentials.
To use a real local emulator, set REDFISH_MOCK_FILE to that emulator's
exported JSON, or set REDFISH_ENDPOINT to a full Redfish thermal URL
such as http://127.0.0.1:8000/redfish/v1/Chassis/1/Thermal
and set REDFISH_USER / REDFISH_PASS in the environment.
No credentials are stored in this repository.
"""
import json
import os
import sys

MOCK_FILE = os.path.join(os.path.dirname(__file__), "mock_thermal.json")


def parse_thermal_data(thermal_data):
    lines = []
    for sensor in thermal_data.get("Temperatures", []):
        name = sensor.get("Name", "Unknown")
        reading = sensor.get("ReadingCelsius", "N/A")
        status = sensor.get("Status", {}).get("Health", "Unknown")
        lines.append(f"Sensor Component: {name} | Temperature: {reading}C | Health: {status}")
    return lines


def main():
    mock_file = os.getenv("REDFISH_MOCK_FILE", MOCK_FILE)
    endpoint = os.getenv("REDFISH_ENDPOINT")
    if endpoint:
        # Only for a local emulator the user explicitly configures.
        # Credentials come from the environment, never from this file.
        user = os.getenv("REDFISH_USER")
        password = os.getenv("REDFISH_PASS")
        if not user or not password:
            print("[ERROR] REDFISH_USER and REDFISH_PASS must be set in the environment to use REDFISH_ENDPOINT.")
            sys.exit(1)
        import requests
        try:
            response = requests.get(endpoint, auth=(user, password), timeout=5)
        except requests.exceptions.RequestException as error:
            print(f"Connection failure to local mock endpoint resource: {error}")
            sys.exit(1)
        if response.status_code != 200:
            print(f"Failed to pull payload. HTTP Status Code: {response.status_code}")
            sys.exit(1)
        thermal_data = response.json()
    else:
        try:
            with open(mock_file, "r", encoding="utf-8") as f:
                thermal_data = json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] Mock thermal file not found: {mock_file}")
            sys.exit(1)
    print("--- Redfish Emulator Telemetry Log (Simulation) ---")
    for line in parse_thermal_data(thermal_data):
        print(line)


if __name__ == "__main__":
    main()
