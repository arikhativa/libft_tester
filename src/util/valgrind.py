#!/bin/python3

from shutil import which

def is_valgrind_installed():
	return which("valgrind") is not None


# run_with_valgrind()
# {
# 	local EXEC=$1

# 	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --log-file=$VALGRIND_OUTPUT ./$EXEC > $USER_RES

# 	local TT=$(grep "ERROR SUMMARY:" $VALGRIND_OUTPUT | awk '{print $4}')

# 	if [ "$TT" == "0" ] ; then
# 		IS_VALGRIND=$SUCCESS
# 	else
# 		IS_VALGRIND=$ERROR
# 	fi
# }
