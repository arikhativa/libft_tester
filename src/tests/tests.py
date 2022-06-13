#!/bin/python3

import single_test
import generic_test

def test_all(path_to_proj):
	t = single_test.testObject("ft_strlen", None, None, None)

	generic_test.test(t, path_to_proj)
