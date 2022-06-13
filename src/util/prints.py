#!/bin/python3

import single_test

def usage() -> None:
	print("libft-tester: illegal option")
	print("usage: make test PROJ=<PROJECT_PATH>")

def norm_error(name: str) -> None:
	print(name + " Error: norm error ")

def no_file(f: single_test.testObject) -> None:
	print("Error: can't find file " + f.name)

def exec_error(f: single_test.testObject) -> None:
	# vaild_res_path=$2
	# user_res_path=$3
	
	print("exec_error")

def print_start_project():
	print("Libft")

# print_compile_error()
# {
# 	test_name=$1

# 	printf "$test_name\t-\tFailed to compile\n" 
# }

# print_valgrind_error()
# {
# 	test_name=$1

# 	printf "$test_name\t-\tValgrind found a memory leak\n" 
# }

# print_no_exec()
# {
# 	local test_name=$1

# 	printf "$test_name\t-\tEmpty dir\n" 
# }

# print_no_dir()
# {
# 	local test_name=$1

# 	printf "Can't find $test_name\n" 
# }


# print_success()
# {
# 	test_name=$1

# 	printf "$test_name\t-\tSuccess!\n" 
# }

# print_norminette_not_installed()
# {
# 	printf "Norminette Error:\n\tapp is not installed!\n\n"
# }

# print_valgrind_not_installed()
# {
# 	printf "Valgrind Error:\n\tapp is not installed!\n\n"
# }