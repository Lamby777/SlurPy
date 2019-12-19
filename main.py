########################################
#            DexieTheSheep             #
#  https://github.com/Lamby777/SlurPy  #
########################################

# Imports
from termcolor import colored
from inspect import signature
from os import system as cmd, name as OS
import math

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

class MetaException(Exception):
	def __init__(self, name):
		self.name = name

oofs = {
	"InvalidCmd": MetaException("Invalid Command!")
}

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

while True:
	print("Type S for shell or R to run code.jc")
	mode = input().lower().strip()
	if mode == "s":
		while True:
			shellJuice = input()
			if not shellJuice in keywords:
				raise oofs.InvalidCmd
	elif mode == "r":
		# Execute Code
		with open("code.jc") as f:
			code = f.read()
			interpret(code)