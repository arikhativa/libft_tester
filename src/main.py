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


import sys

import src
import print
import strings


def main():
	if (len(sys.argv) != 2):
		print.print_usage()
		return
	
	strings.test_strings()

	
	

main()