########################################
#            DexieTheSheep             #
#  https://github.com/Lamby777/SlurPy  #
########################################

# Imports
from termcolor import colored
from error import oof
import fn, math

# Hoisted Functions

def cmdHelp():
	print("\n")
	[print(i + "\n-> " + cmds[i][1] + "\n") for i in cmds]
	print("\n")

# Constants
ops = {
	"ps": lambda x, y: x+y,
	"sb": lambda x, y: x-y,
	"mt": lambda x, y: x*y,
	"dv": lambda x, y: x/y,
	"pw": lambda x, y: x**y,
	"sq": lambda x: math.sqrt(x),
}
keywords = [i for i in ops]

cmds = {
	"help": [cmdHelp, "Lists all commands"],
	"echo": [lambda x: print(x), "Prints to terminal"],
	"clear": [fn.cls, "Clears terminal"],
	"script": [fn.runJuice, "Runs file"],
}

print(colored("Welcome to SlurpTerminal"))
while True:
	print(">", end=" ")
	cmdfull = input().lower().strip().split(" ")
	cmd = cmdfull[0]
	if not cmd in cmds:
		fn.out("Invalid Command! Use \"help\"", "red")
	else:
		cmdargs = " ".join(cmdfull[1:])
		cmds[cmd][0](cmdargs)
