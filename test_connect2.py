#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass


device1 = {
       'host': 'cisco3.lasthop.io',
       'username': 'pyclass',
      'password': getpass(),
      'device_type': 'cisco_xe',
      #session_log:'my_session.txt'
      }
device2 = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type': 'cisco_xe'
        }

device_list = [device1, device2]

for device in device_list:
    net_connect = ConnectHandler(** device)
    print(net_connect.find_prompt())
