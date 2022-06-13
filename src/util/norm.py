#!/bin/python3

from shutil import which
import subprocess
import prints

def is_norminette_installed():
	return which("norminette") is not None

def norm(name: str, path: str, flags: str="-R CheckForbiddenSourceHeader") -> None:
	text = "norminette {flags} {src}"

	cmd = text.format(flags=flags, src=path)
	out = subprocess.run(cmd.split(), capture_output=True)

	if "Error" in str(out.stdout) or "Warning" in str(out.stdout):
		prints.norm_error(name)

