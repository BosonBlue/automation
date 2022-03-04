#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='cisco3.lasthop.io', username='pyclass', password='88newclass', device_type='cisco_xe', session_log='debug.txt')


output = new_conn.send_config_from_file("cfg.txt")

google_ping = new_conn.send_command('ping google.com')

new_conn.disconnect()

print(output)
print(google_ping)

