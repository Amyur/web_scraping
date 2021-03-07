import subprocess

subprocess.call(['python', 'extract.py'], cwd="./Extract")
subprocess.call(['python', 'transform.py'], cwd="./Transform")
subprocess.call(['python', 'main.py'], cwd="./Load")
