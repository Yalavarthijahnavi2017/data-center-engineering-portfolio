# Data Center Engineering & Automation Simulation Lab (2026)

This repository serves as a centralized portfolio for my independent infrastructure automation, out-of-band management scripting, and network simulation projects. All projects contained here are executed within localized virtual machines and software emulator sandboxes.

This repository contains independently developed and documented projects involving Linux server administration, data center hardware maintenance, infrastructure automation, networking, Python Redfish API integration, Ansible and AWS cloud infrastructure.

The projects include hands-on technical demonstrations, virtual environments, simulated hardware data and independently deployed cloud resources.

All projects will be accurately labeled according to their execution environment. Simulated and emulator-based projects will not be presented as production or commercial data center experience.

## Current Projects
1. **Ansible Playbook Simulation (`/ansible-playbooks/`):** Automated package baseline configuration targeting a virtual cluster.
2. **Out-of-Band Telemetry Scripting (`/python-scripts/`):** Python scripts interfacing with standard RESTful Redfish API chassis emulators.
3. **Network Topology Design (`/network-topologies/`):** Access-layer routing, dynamic VLAN tagging, and ACL setups simulated inside Cisco Packet Tracer.

## Status
- Physical Dell PowerEdge / RAID / Linux / iDRAC experience is separate from these independent projects.
- Simulated and emulator-based work is labeled as such.
- Terraform and AWS work will be added only after it is built and tested locally.

## Directory Layout
- `/ansible-playbooks/` - System configuration lifecycles and server baselines (virtual simulation cluster, example targets only).
- `/python-scripts/` - Programmatic out-of-band chassis management and log analytics (mock JSON by default, no hardcoded credentials).
- `/network-topologies/` - Cisco Packet Tracer configuration blueprints (simulation only; no Packet Tracer project files uploaded yet).
