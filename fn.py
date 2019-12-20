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
	print(colored(msg, color))