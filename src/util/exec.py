
import subprocess

def exec(exec_path):
	process = subprocess.Popen(exec_path, stdout=subprocess.PIPE)
	_, error = process.communicate()
	if (error != None):
		print(error)
		return ERROR
	return SUCCESS
