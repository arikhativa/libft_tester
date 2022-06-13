#!/bin/python3

import subprocess

def compile(name, path_to_src):
	bashCommand = "gcc -Wall -Werror -Wextra -I {path_to_src} /home/yoav/libft_tester/src/tests/{name}/main.c {path_to_src}/libft.a"
	cmd = bashCommand.format(name=name, path_to_src=path_to_src)
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	_, error = process.communicate()
	if (error != None):
		print(error)
		return ERROR
	return SUCCESS


# compile_tests()
# {
# 	local MAIN=$1
# 	local USR_SRC=$2
	

# 	local err_msg=$(gcc -Wall -Werror -Wextra $MAIN/*.c $USR_SRC/*.c)
	
# 	if [ ! -e $EXEC_FIEL ] ; then
# 		IS_COMPLIE=$ERROR
# 	else
# 		IS_COMPLIE=$SUCCESS
# 	fi
# }

# compile_tests_c08()
# {
# 	local MAIN=$1
# 	local USR_SRC=$2
# 	C_INCLUDE_PATH=$C_INCLUDE_PATH:$USR_SRC:$MAIN
# 	CPATH=$CPATH:$USR_SRC:$MAIN

# 	if [[ "$USR_SRC" == *"ex04"* || "$USR_SRC" == *"ex05"* ]] ; then
# 		local err_msg=$(gcc -Wall -Werror -Wextra -I $MAIN $USR_SRC/*.c $MAIN/*.c)
# 	else
# 		local err_msg=$(gcc -Wall -Werror -Wextra -I $USR_SRC $MAIN/*.c)
# 	fi
	
# 	if [ ! -e $EXEC_FIEL ] ; then
# 		IS_COMPLIE=$ERROR
# 	else
# 		IS_COMPLIE=$SUCCESS
# 	fi
# }

# compile_tests_c06()
# {
# 	local USR_SRC=$1

# 	local err_msg=$(gcc -Wall -Werror -Wextra $USR_SRC -o $UNIQUE_EXEC)
# 	if [ ! -e $UNIQUE_EXEC ] ; then
# 		IS_COMPLIE=$ERROR
# 	else
# 		IS_COMPLIE=$SUCCESS
# 	fi
# }
