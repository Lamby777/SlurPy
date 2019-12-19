from inspect import signature
from os import system as runTerminal, name as OS
from termcolor import colored

def params(fn):
	return len(signature(fn).parameters)

def runJuice(x="code.jc"):
	with open(x) as f:
		code = f.read()
		interpret(code)

def cls():
	if OS == 'nt':
		runTerminal('cls')
	else:
		runTerminal('clear')

def tokenize(code):
	tokens = []
	return tokens

def interpret(code):
	return tokenize(code)

def out(msg, color="white"):
	print(colored(msg, color))