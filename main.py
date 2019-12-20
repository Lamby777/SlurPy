########################################
#            DexieTheSheep             #
#  https://github.com/Lamby777/SlurPy  #
########################################

# Imports
from termcolor import colored
import fn, error, math

# Hoisted Functions

def cmdHelp():
	print("\n" + "\n".join(
		[i + "\n-> " + cmds[i][1] + "\n" for i in cmds]
	))

def runJuice(x="code.jc"):
	try:
		with open(x) as f:
			code = f.read()
			interpret(code)
	except FileNotFoundError:
		print(colored("Your will now execute. "
		"In the future, please\n"
		"add the .jc to the end of the file name.", "red"))
		try:
			with open(x + ".jc") as f:
				code = f.read()
				interpret(code)
		except FileNotFoundError:
			print(colored("Error: File not Found!", "red"))

def tokenize(code):
	tokens = []
	return tokens

def interpret(code):
	for x in tokenize(code):
		pass

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
	"script": [runJuice, "Runs file"],
}

print(colored("Welcome to SlurpTerminal"))
while True:
	print(">", end=" ")
	cmdfull = input().lower().strip().split(" ")
	cmd = cmdfull[0]
	if not cmd in cmds:
		fn.out("Error: Invalid Command! Use \"help\"", "red")
	else:
		cmdargs = " ".join(cmdfull[1:])
		replFn = cmds[cmd][0]
		if cmdargs: replFn(cmdargs)
		else: replFn()
