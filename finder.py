import subprocess

n = subprocess.check_output(['iwlist', 'scan'])
print(n.decode('utf-8'))
