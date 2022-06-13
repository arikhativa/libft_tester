#!/bin/python3

import testObject

def test_strings():
	t = testObject.testObject("ft_putchar", 1)
	print(t.name)

	# TESTS_NAMES=(ft_putchar ft_print_alphabet ft_print_reverse_alphabet ft_print_numbers ft_is_negative ft_print_comb ft_print_comb2 ft_putnbr ft_print_combn )
	# local NUM_OF_FILES_PER_TEST=(1 1 1 1 1 1 1 1 1)

	# generic_project_test "c00" $TESTS_NAMES $NUM_OF_FILES_PER_TEST
