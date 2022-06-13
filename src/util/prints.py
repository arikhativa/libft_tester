#!/bin/python3

import single_test

def no_file(f: single_test.testObject):
	print("Error: can't find file " + f.name)

def usage():
	print("libft-tester: illegal option")
	print("usage: make test PROJ=<PROJECT_PATH>")

# print_start_project()
# {
# 	project_name=$1

# 	printf "\n -- Testing project $project_name -- \n\n"
# }

# print_compile_error()
# {
# 	test_name=$1

# 	printf "$test_name\t-\tFailed to compile\n" 
# }

# print_norm_error()
# {
# 	test_name=$1

# 	printf "$test_name\t-\tNot following the norm\n" 
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

# print_fail()
# {
# 	test_name=$1
# 	vaild_res_path=$2
# 	user_res_path=$3
	
# 	printf "$test_name\t-\tFail\n\n"
# 	printf "Expected output:\n"
# 	printf "%s$(cat $vaild_res_path)\n\n"
# 	printf "User  output:\n"
# 	printf "%s$(cat $user_res_path)\n"
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