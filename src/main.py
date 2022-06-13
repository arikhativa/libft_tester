#!/bin/python3

# class MyClass:
#   x = 5

# EXEC_FIEL="a.out"
# USER_RES=./user_res.txt
# IS_DIFF_FILE=./is_diff
# VALGRIND_OUTPUT=./valgrind_output.txt
# UNIQUE_EXEC="ppp.out"

# SUCCESS=1
# ERROR=0
# IS_COMPLIE=$ERROR
# IS_NORM=$ERROR
# IS_NORMINETTE=$ERROR
# IS_VALGRIND=$ERROR
# IS_VALGRIND_INSTALLED=$ERROR

# FILES_IN_DIR=0

# BASEDIR=$(dirname "$0")

# if [ "$USER_REPO_PATH" == "" ] ; then
# 	USER_REPO_PATH="$BASEDIR/../"
# fi

# is_norminette_installed
# is_valgrind_installed


from sre_constants import SUCCESS
import sys

sys.path.append("./src/util")
sys.path.append("./src/tests")

import norm
import valgrind
import prints
import tests

# Globals
ERROR					= False
SUCCESS					= True
IS_NORM_INSTALLED		= ERROR
IS_VALGRIND_INSTALLED	= ERROR
VALGRIND_OUTPUT			= "valgrind.txt"
EXEC					= "a.out"
USER_OUTPUT				= "user_output.txt"

def main():
	if (len(sys.argv) != 2):
		prints.usage()
		return

	is_norm_installed = norm.is_norminette_installed()
	is_valgrind_installed = valgrind.is_valgrind_installed()

	tests.test_all(sys.argv[1], is_norm_installed, is_valgrind_installed)

	
	

main()