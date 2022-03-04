#!/usr/bin/env python


from netmiko import ConnectHandler
from getpass import getpass


devices = (

    {'host':'nxos1.lasthop.io', 'username':'pyclass', 'password':'88newclass', 'device_type':'cisco_nxos'}

)
new_conn = ConnectHandler(** devices)

print(new_conn.find_prompt())




