#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

devices = (

     {'host':'nxos1.lasthop.io', 'username':'pyclass', 'password':'88newclass', 'device_type':'cisco_nxos'},
     {'host':'nxos2.lasthop.io', 'username':'pyclass', 'password':'88newclass', 'device_type':'cisco_nxos'}
 )


for device in devices:

   

    new_conn = ConnectHandler(** device)
    
    print(new_conn.find_prompt())

