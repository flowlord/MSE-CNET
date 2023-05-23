"""

USE ON WINDOWS ONLY

DeepBooru
"""



import shutil
import zipfile
import os
import subprocess
import ntpath



def genesis(x):
	for i in range(x):
		file_name = f"Cx/mse_base_{i}.zip"
		shutil.copy("mse_base_.zip", file_name)
		zipfile.ZipFile(file_name, mode = "r").extractall(f"Cx/mse_base_{i}")
		os.remove(file_name)


def reset():
	path_name = "Cx/"
	path = os.listdir(path_name)

	for file in path:
		os.remove(path_name+file)


n = 3


def cxcrypt(msg):
	for e in range(n):
		cmd = f'cd Cx && cd mse_base_{e} && MSE.py c "{msg}"'
		run_cmd = subprocess.run(cmd, shell=True, capture_output=True, text=True)


def cxdecrypt():
	for e in range(n):
		cmd = f'cd Cx && cd mse_base_{e} && MSE.py d'
		run_cmd = subprocess.run(cmd, shell=True, capture_output=True, text=True)
		print(run_cmd.stdout)


def copy_code():

    z = [os.path.join(root, f) for root, _, files in os.walk("Cx/") for f in files]
    z = [x.replace('\\','/') for x in z]

    c = 0

    for e in z:
    	if "ct.txt" in e:
    		shutil.copy(e,f"result/{c}"+ntpath.basename(e))
    		c = c+1



genesis(n)
cxcrypt("hello world")
cxdecrypt()


copy_code()





