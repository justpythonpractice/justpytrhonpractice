#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2, arg3 = args
	print("arg1: %r, arg2: %r, arg3: %r" % (arg1,arg2, arg3))

#again but without *args
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))

#this just takes one argument
def print_one(arg1):
	print("arg1: %r" % arg1)

#this one takes no argument
def print_none():
	print("I got nuffin.")

print_two("zed", "shaw", 15)
print_two_again("Zed","SHAW")
print_one("FIRST!")
print_none()