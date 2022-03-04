#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='nxos2.lasthop.io', username='pyclass', password='88newclass', device_type='cisco_xe', global_delay_factor=8, session_log='debug.txt')

output = new_conn.send_command('show lldp neighbors detail')


new_conn.disconnect()

print(output)


