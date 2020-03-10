"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open('foo.txt', 'r')
for line in f:
    print(line, end='')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
g = open('bar.txt', 'w')
g.write('Hello, new file here. How are you?\n')
g.write("Anyone there? If you're there it's hard to see you in this infinite void.\n")
g.write("... I am so, totally alone.\n")
g.close()

g = open('bar.txt', 'r')
for line in g:
    print(line, end='\n')