
import paramiko

key = paramiko.RSAKey.from_private_key_file('/home/itachi/Dropbox/JOB/FLAPPER/Infra/VM_KEYS/prd_key.pem')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='35.170.72.129', username='ubuntu', pkey=key)

commands = [

    'sudo apt-get update -y',
    'sudo apt-get install -y python3-pip',

    'git clone https://github.com/williamloliveira/dashboard-1.git',

    'sudo pip3 install -r dashboard-1/requirements.txt',
    'sudo python3 dashboard-1/app.py'

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())