### Virtual Cluster Baseline Configuration
This module uses Ansible to provision standard utility packages across targeted test nodes. Simulation only - virtual hosts, not production servers.

- `inventory.ini`: Configures virtual test target IPs (example private addresses 192.168.10.11-13, hosts sim-node01/02/03.local) for the virtual simulation cluster.
- `site.yml`: Enforces standard system utilities (`ethtool`, `smartmontools`, `net-tools`) and configures virtual syslog forwarding to `virtual-collector.local:514` via `/etc/rsyslog.d/60-simulation-forward.conf`, with a handler to restart rsyslog.

Tested locally: `ansible-playbook --syntax-check -i inventory.ini site.yml` passes. Not executed on real hosts.
