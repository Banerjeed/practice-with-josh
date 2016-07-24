"""
hello
string
comment
"""

#num1 = 5
#num2 = 10
#print (num1+num2)
name1 = raw_input('what is your name?')
age1 = int(raw_input('how old are you %s?' % name1))
if age1>=21:
	print "you can drink wine!"
elif age1 <0:
	print "invalid"
else:
	print "LOSER"	

print 'this line was added by josh'
