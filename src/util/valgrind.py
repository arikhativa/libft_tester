#!/bin/python3

from shutil import which
import single_test

def is_valgrind_installed():
	return which("valgrind") is not None

def run_with_valgrind(f: single_test.testObject):
	s = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --log-file={out} ./{exec} > {res}"
	cmd = s.format(out=VALGRIND_OUTPUT, exec=EXEC, res=USER_OUTPUT)
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	_, error = process.communicate()
	if (error != None):
		print(error)
		return ERROR

	cmd = "grep 'ERROR SUMMARY:' {f} | awk '{print $4}'"
	process = subprocess.Popen(cmd.format(f=VALGRIND_OUTPUT), stdout=subprocess.PIPE)
	is_valgrind, error = process.communicate()
	if (error != None):
		print(error)
		return ERROR

	print(is_valgrind)
	