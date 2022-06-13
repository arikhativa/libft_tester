#!/bin/python3

from shutil import which
import subprocess

def is_norminette_installed():
	return which("norminette") is not None

def norm(src, path_to_project, flags="-R CheckForbiddenSourceHeader"):
	bashCommand = "norminette {flags} {path_to_project}/{src}"
	cmd = bashCommand.format(flags=flags, path_to_project=path_to_project, src=src)
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	_, error = process.communicate()
	if (error != None):
		print(error)
		return ERROR
	return SUCCESS
