# -----------------------------------------------------------------------
"""
Uses ipaddress module to ask for an IP address and check to validate it is in the correct format.
"""

import ipaddress

# Enter IP address
ip_network_address = input('Enter the IP address: ')
ip_network_address = ipaddress.IPv4Address(ip_network_address)

# Create a list and populate it with the IP range
ip_address_of_wlc = str(ip_network_address)
# -----------------------------------------------------------------------