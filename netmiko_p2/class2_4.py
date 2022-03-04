#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

new_conn = ConnectHandler(host='cisco3.lasthop.io', username='pyclass', password='88newclass', device_type='cisco_xe', session_log='debug.txt')

cfg = ['ip name-server 1.1.1.1',
        'ip name-server 1.0.0.1',
        'ip domain-lookup'
]

output = new_conn.send_config_set(cfg)
output += new_conn.send_command('ping 8.8.8.8')


new_conn.disconnect()

print(output)


