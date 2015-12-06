f = open('myfile', 'r')
f = open('myfile', 'w')

try:
    f = open('myfile')
except IOError:
    print("does not exist")

for line in f:
    print(line)

f.read()      # nothing left
f.seek(0)     # reset pointer
f.read()      # read all lines
f.seek(0)
f.readline()  # read one line at a time

f.open('path/myfile', 'a')  # append
f.write('this is the string to append')
f.close()
