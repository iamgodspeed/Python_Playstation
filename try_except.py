astr = 'Hello'
try:
    print 'print anyway'
    test = int(astr)
except:
    test = -1
print 'first', test

astr = 'Hello2'
try:
    print 'before explosion'
    test = int(astr)
except:
    test = -2
print 'second', test

