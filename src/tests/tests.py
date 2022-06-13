#!/bin/python3

import prints
import single_test
import generic_test

def test_all(path_to_proj: str, is_norm: bool, is_valgrind: bool):
	t = single_test.testObject("ft_strlen", None, None, None)

	prints.print_start_project()
	generic_test.test(t, path_to_proj, is_norm, is_valgrind)
