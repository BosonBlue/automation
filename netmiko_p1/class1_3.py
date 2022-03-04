#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass


device1 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_nxos',
    #session_log:'my_session.txt'
    }
new_conn = ConnectHandler(** device1)

output = new_conn.send_command('show version')

print(output)



