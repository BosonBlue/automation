import paramiko
import time
from pprint import pprint

router_ip = 'cisco3.lasthop.io'
router_username = 'pyclass'
router_password = '88newclass'


ssh = paramiko.SSHClient()

# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
ssh.connect(router_ip, 
            username=router_username, 
            password=router_password,
            look_for_keys=False )

# Run command.
stdin, stdout, stderr = ssh.exec_command("show version")
time.sleep(1)
stdout.channel.set_combine_stderr(True)
output = stdout.readlines()
pprint(output)
# Close connection.
ssh.close()
