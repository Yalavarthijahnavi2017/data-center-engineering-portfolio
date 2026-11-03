### Out-of-Band Telemetry Scripting - Simulation Only

Python scripts for out-of-band management and system diagnostics, tested against local mock data. No credentials are stored in this repository.

- `redfish_monitor.py`: Parses Redfish-style thermal data. By default it reads the local `mock_thermal.json` file (Inlet / CPU temperatures, Health status). To use a local emulator, set `REDFISH_ENDPOINT` to a full thermal URL and `REDFISH_USER` / `REDFISH_PASS` in the environment - credentials are never committed.
- `mock_thermal.json`: Sample Redfish thermal payload used for local testing.
- `log_parser.py`: Scans a log file for hardware error, mce, pcie fault, link down, and drive degraded keywords. Default `/var/log/messages`; pass a sample file as an argument for testing, e.g. `python3 log_parser.py sample_messages.log`.
- `sample_messages.log`: Sample log used for local testing.

Tested locally: Redfish mock parser prints 3 sensors; log parser matches 3 alert lines on the sample log and ignores normal lines.
