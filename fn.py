from inspect import signature
from os import system as runTerminal, name as OS
from termcolor import colored

def params(fn):
	return len(signature(fn).parameters)

def cls():
	if OS == 'nt':
		runTerminal('cls')
	else:
		runTerminal('clear')

def out(msg, color="white"):
	if isinstance(msg, list):
		print("-> " + msg.pop() + [
			"\n^-" + line for line in msg
		])
	else:
		print("-> " + colored(msg, color))
