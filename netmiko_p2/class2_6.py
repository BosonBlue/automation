#!/usr/bin/env python

import time
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = getpass()

new_conn = ConnectHandler(host='cisco4.lasthop.io', username='pyclass', password=password, secret=password, device_type='cisco_ios', session_log='debug.txt')


output = new_conn.find_prompt()
output += new_conn.config_mode()
output += new_conn.find_prompt()
output += new_conn.exit_config_mode()
output += new_conn.find_prompt()
new_conn.write_channel("disable\n")
output += new_conn.find_prompt()
time.sleep(2)
output1 = new_conn.read_channel()


new_conn.disconnect()

print(output)
print(f'read channel is {output1}')

