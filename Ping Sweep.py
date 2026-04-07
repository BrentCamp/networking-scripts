#!/usr/bin/env python3
"""
ping_sweep.py
Author: Brent Camp
Description: Sweep a subnet and report which hosts are up or down.
Usage: python3 ping_sweep.py
Requires: Python 3.6+
Note: May require elevated privileges on some systems.
"""

import ipaddress
import subprocess
import platform
import concurrent.futures
from datetime import datetime


def ping_host(ip):
    """Ping a single host. Returns (ip, is_up)."""
    system = platform.system().lower()

    # -c 1 for Linux/macOS, -n 1 for Windows. -W/-w sets timeout in seconds.
    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return (str(ip), result.returncode == 0)


def sweep_subnet(subnet_input, max_workers=50):
    try:
        network = ipaddress.IPv4Network(subnet_input, strict=False)
    except ValueError as e:
        print(f"\n[ERROR] Invalid subnet: {e}")
        print("Example: 192.168.1.0/24\n")
        return

    hosts = list(network.hosts())

    if not hosts:
        print("[INFO] No usable hosts in this subnet.")
        return

    print(f"\n{'=' * 50}")
    print(f"  Ping Sweep: {subnet_input}")
    print(f"  Scanning {len(hosts)} hosts — started {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'=' * 50}\n")

    up_hosts   = []
    down_hosts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(ping_host, host): host for host in hosts}
        for future in concurrent.futures.as_completed(futures):
            ip, is_up = future.result()
            if is_up:
                up_hosts.append(ip)
                print(f"  [UP]   {ip}")
            else:
                down_hosts.append(ip)

    print(f"\n{'=' * 50}")
    print(f"  Sweep Complete — {datetime.now().strftime('%H:%M:%S')}")
    print(f"  Hosts UP  : {len(up_hosts)}")
    print(f"  Hosts DOWN: {len(down_hosts)}")
    print(f"{'=' * 50}\n")


def main():
    print("\n--- Ping Sweep ---")
    print("Enter a subnet in CIDR notation (e.g. 192.168.1.0/24)")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Subnet: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Exiting. Goodbye.")
            break
        if not user_input:
            continue
        sweep_subnet(user_input)


if __name__ == "__main__":
    main()