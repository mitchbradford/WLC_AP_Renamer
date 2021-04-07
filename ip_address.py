# -----------------------------------------------------------------------
"""
Uses ipaddress module to ask for an IP address and check to validate it is in the correct format.
"""

import ipaddress

while True:
	try:
		ip_network_address = ipaddress.ip_address(input('Enter IP address: '))
		break
	except ValueError:
		print('Please enter a valid IP Address')
		continue

# Create a list and populate it with the IP range
ip_address_of_wlc = str(ip_network_address)
# -----------------------------------------------------------------------