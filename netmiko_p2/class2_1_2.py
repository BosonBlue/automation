#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='cisco4.lasthop.io', username='pyclass', password=getpass(), device_type='cisco_xe', session_log='debug.txt')


output = new_conn.send_command_timing('ping')
output += new_conn.send_command_timing('ip')
output += new_conn.send_command_timing('8.8.8.8')
output += new_conn.send_command_timing('5')
output += new_conn.send_command_timing('100')
output += new_conn.send_command_timing('2')
output += new_conn.send_command_timing('n')
output += new_conn.send_command_timing('n')



new_conn.disconnect()

print(output)


