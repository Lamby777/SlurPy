########################################
#            DexieTheSheep             #
#  https://github.com/Lamby777/SlurPy  #
########################################

# Imports
from termcolor import colored
from inspect import signature
from os import system as cmd
from os import name as OS

# Constants
ops = [
	[]
]

# Functions

def params(fn):
	return len(signature(fn).parameters)

def cls():
	if OS == 'nt':
		cmd('cls')
	else:
		cmd('clear')

def tokenize(code):
	tokens = []
	return tokens

def interpret(code):
	return tokenize(code)

def out(msg, color):
	print(colored(msg, color))

# Execute Code
with open("code.jc") as f:
	code = f.read()
	interpret(code)