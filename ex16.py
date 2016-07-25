#expecting variables from console
from sys import argv

#adding our vars to the array argv
script, filename = argv

print("We're going to erase %r" % filename)
#stop the programm if you don't want to proceed with flushing
print("if you don't want that, hit CTRL-C (^C).")

print("If you do want that, hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()
#input what will be put into the file
print ("Now i'm going to ask you for three lines.")
line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print("I'm going to write these to the file.")
#writing
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#closing
print("and finally, we close it!")
target.close()
