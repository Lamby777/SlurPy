########################################
#            DexieTheSheep             #
#  https://github.com/Lamby777/SlurPy  #
########################################

# Imports
from termcolor import colored
import os.system as cmd, os.name as OSName

# Functions

def cls():
    if OSName == 'nt':
        cmd('cls')
    else:
        cmd('clear')

def tokenize(code):
    pass

def interpret(code):
    return tokenize(code)
    # will improve code

# Execute Code
with open("code.jc") as f:
    pass