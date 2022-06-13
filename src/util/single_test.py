#!/bin/python3

import compile as c
import exec as e
import norm as n

class testObject:
	name: str
	compile: object
	norm: object
	exec: object

	def __init__(self, name, compile, norm, exec):
		self.name = name
		
		if (compile == None):
			compile = c.compile
		if (norm == None):
			norm = n.norm
		if (exec == None):
			exec = e.exec

		self.compile = compile
		self.norm = norm
		self.exec = exec
