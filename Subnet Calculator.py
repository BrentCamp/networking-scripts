#!/usr/bin/env python3
"""
subnet_calculator.py
Author: Brent Camp
Description: Calculate subnet details from an IP address and prefix length.
Usage: python3 subnet_calculator.py
"""

import ipaddress


def calculate_subnet(ip_input):
    try:
        network = ipaddress.IPv4Network(ip_input, strict=False)

        network_addr = str(network.network_address)
        broadcast    = str(network.broadcast_address)
        subnet_mask  = str(network.netmask)
        prefix       = network.prefixlen
        num_hosts    = network.num_addresses - 2 if network.num_addresses > 2 else 0
        first_host   = str(network.network_address + 1) if num_hosts > 0 else "N/A"
        last_host    = str(network.broadcast_address - 1) if num_hosts > 0 else "N/A"

        print("\n" + "=" * 45)
        print(f"  Subnet Details for: {ip_input}")
        print("=" * 45)
        print(f"  Network Address  : {network_addr}/{prefix}")
        print(f"  Subnet Mask      : {subnet_mask}")
        print(f"  Broadcast        : {broadcast}")
        print(f"  First Usable Host: {first_host}")
        print(f"  Last Usable Host : {last_host}")
        print(f"  Usable Hosts     : {num_hosts:,}")
        print("=" * 45 + "\n")

    except ValueError as e:
        print(f"\n[ERROR] Invalid input: {e}")
        print("Example valid inputs: 192.168.1.0/24  or  10.0.0.50/16\n")


def main():
    print("\n--- Subnet Calculator ---")
    print("Enter an IP address with prefix length (e.g. 192.168.1.0/24)")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("IP/Prefix: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Exiting. Goodbye.")
            break
        if not user_input:
            continue
        calculate_subnet(user_input)


if __name__ == "__main__":
    main()