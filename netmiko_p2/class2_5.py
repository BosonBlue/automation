#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='nxos1.lasthop.io', username='pyclass', password='88newclass', device_type='cisco_nxos', session_log='debug.txt')


output = new_conn.send_config_from_file("vlan.txt")


new_conn.disconnect()

print(output)


