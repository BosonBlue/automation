#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='cisco4.lasthop.io', username='pyclass', password='88newclass', device_type='cisco_ios', session_log='debug.txt')

output = new_conn.send_command('show lld neighbors', use_textfsm=True)


new_conn.disconnect()

print(output)

print (f"the adjecent router is connected to port {output[0]['local_interface']}")

