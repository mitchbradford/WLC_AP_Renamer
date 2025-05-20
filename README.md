# WLC_AP_Renamer

Python script to rename APs on a Cisco WLC based on a CSV file using Netmiko

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
Python 3
Netmiko Python Library
```

### Installing

Install the Netmiko Python Library

## Running the script
```
git clone https://github.com/mitchbradford/WLC_AP_Renamer.git 
cd  WLC_AP_Renamer
```
Populate CSV in the following format "hostname,mac,serial"
```
python run.py
```
## Version 1.0
Added support for Cisco vWLC and C9800 WLCs

## Version 0.1
Initial Release

## Authors

* **Mitch Bradford** - [Github](https://github.com/mitchbradford)

## License

This project is licensed under the GNU GPLv3 License.

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/mitchbradford/WLC_AP_Renamer)
