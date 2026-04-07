# Networking Scripts

A collection of Python scripts for network analysis, discovery, and automation. Built for practical NOC and network operations use cases.

---

## Scripts

### 1. Subnet Calculator
**File:** `subnet_calculator.py`

Calculates subnet details from an IP address and prefix length.

**Output includes:**
- Network address
- Subnet mask
- Broadcast address
- First and last usable host
- Total usable host count

**Usage:** `python3 subnet_calculator.py`

**Example input:** `192.168.10.0/24`

**Example output:**

> Network Address   : 192.168.10.0/24
> Subnet Mask       : 255.255.255.0
> Broadcast         : 192.168.10.255
> First Usable Host : 192.168.10.1
> Last Usable Host  : 192.168.10.254
> Usable Hosts      : 254

---

### 2. Ping Sweep
**File:** `ping_sweep.py`

Sweeps a subnet and reports which hosts are up or down using concurrent threading for fast results.

**Output includes:**
- Real-time up/down status per host
- Total hosts up and down at completion
- Timestamp for sweep start and end

**Usage:** `python3 ping_sweep.py`

**Example input:** `192.168.10.0/24`

**Example output:**

> Scanning 254 hosts — started 14:32:01
> [UP]   192.168.10.1
> [UP]   192.168.10.5
> [UP]   192.168.10.22
> Sweep Complete — Hosts UP: 3 | Hosts DOWN: 251

**Note:** May require elevated privileges on some systems.

---

## Requirements

- Python 3.6+
- No external libraries required — standard library only

---

## Planned Additions

- Port scanner
- SSH device logger
- Uptime monitor with timestamped logging

---

## Author

**Brent Camp**
- [LinkedIn](https://www.linkedin.com/in/brentcamp2)
- [GitHub](https://github.com/BrentCamp)
