#!/usr/bin/env python

import time
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = getpass()

new_conn = ConnectHandler(host='cisco4.lasthop.io', username='pyclass', password=password, secret=password, device_type='cisco_ios', session_log='debug.txt')


new_conn.write_channel("show ip int brief\n")

time.sleep(2)

output = new_conn.read_channel()


print(output)
print(f'read channel is {output}')

new_conn.disconnect()

