#!/usr/bin/env python
# Script by Mitch Bradford
# Dependencies - Netmiko, Python 3
# Instructions - list AP MAC Addresses and hostname in aps.csv

# -----------------------------------------------------------------------
import os.path
from ip_address import ip_address_of_wlc as ip_address_of_wlc
from datetime import datetime
from netmiko import ConnectHandler
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from getpass import getpass
from pprint import pprint
import csv

# -----------------------------------------------------------------------

username = input('Enter your username:')
password = getpass("Enter your password: ")
aps = csv.DictReader(open("aps.csv"))

# -----------------------------------------------------------------------

def rename_devices(ip_of_wlc):
	"""
	Function using Netmiko to connect to each of the devices
	"""

	# Network device definition for Netmiko
	ios_device = {
	'device_type': 'cisco_ios',
	'ip': ip_address_of_wlc,
	'username': username,
	'password': password,
	}
	
	# Connect to device, run commands
	try:
		current_time = datetime.now().strftime("%y_%m_%d_%H%M")
		
		print ('Connecting to device ' + ip_address_of_wlc)
		remote_conn = ConnectHandler(**ios_device)
		remote_conn.send_command("xx")
		
		for row in aps:
			print("mac:",row['mac'])
			print("hostname:",row['hostname'])
			#connect(row['hostname'])
			print(ip_address_of_wlc)
			
		# Cleanly disconnect SSH session	
		remote_conn.disconnect()
		
	except IndexError as e:
		print("No line in the CSV:", e)
		pass
		
def main():
	"""
	Call functions to run the script.
	Record the amount of time required to do this.
	"""
	start_time = datetime.now()

	rename_devices(ip_address_of_wlc)
	
	print("\nElapsed time: " + str(datetime.now() - start_time))

if __name__ == "__main__":
	main()
