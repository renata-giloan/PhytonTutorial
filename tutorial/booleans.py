# b = None
# b = 'games'
# print b

print 1 < 5 < 3
a = 1
b = '1'
print a != b
a = 3
b = '100'
print True and False

x = True
if x:
    print 'X was True!'
else:
    print 'X is not True!'

l = [2, 5, 8, 13, 15, 19, 22, 25, 29]
a = []
b = []
c = []
for i in l:
    if i < 10:
        a.append(i)
    elif i < 20:
        b.append(i)
    else:
        c.append(i)
    # print "when i is: " + str(i) + "; a is " + str(a) + "; b is " + str(b) + "; c is " + str(c)
print 'a is: ' + str(a) + '; b is: ' + str(b) + '; c is: ' + str(c)