########################################
#            DexieTheSheep             #
#  https://github.com/Lamby777/SlurPy  #
########################################

# Imports
from termcolor import colored
from error import oof
import fn, math

# Constants
ops = [
	["ps", lambda x, y: x+y],
	["sb", lambda x, y: x-y],
	["mt", lambda x, y: x*y],
	["dv", lambda x, y: x/y],
	["pw", lambda x, y: x**y],
	["sq", lambda x: math.sqrt(x)],
]
keywords = [i[0] for i in ops]

cmds = [
	["echo", lambda x: print(x)],
	["clear", fn.cls],
	["script", fn.runJuice],
]
cmdk = [i[0] for i in cmds]

while True:
	print(colored("Welcome to SlurpTerminal"))
	cmd = input().lower().strip()
	if cmd in cmdk:
		while True:
			print("> ", end="")
			shellJuice = input()
			if not shellJuice in keywords:
				raise oof["InvalidCmd"]