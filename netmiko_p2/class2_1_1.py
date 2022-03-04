#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='cisco4.lasthop.io', username='pyclass', password=getpass(), device_type='cisco_xe', session_log='debug.txt')

output = new_conn.send_command('ping', expect_string=r'ip')
output += new_conn.send_command('ip', expect_string=r'address')
output += new_conn.send_command('8.8.8.8', expect_string=r'5')
output += new_conn.send_command('5', expect_string=r'100')
output += new_conn.send_command('100', expect_string=r'2')
output += new_conn.send_command('2', expect_string=r'n')
output += new_conn.send_command('n', expect_string=r'n')
output += new_conn.send_command('n', expect_string=r'#')


new_conn.disconnect()

pprint(output)


