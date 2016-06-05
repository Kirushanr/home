def print_two(*args):
	arg1,arg2 = args
	print "arg1: %r, arg2:%r" % (arg1,arg2)
#def stands for define
#define a function called prin_two_again	
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_one(arg1):
	print "arg1 : %r" % arg1

def print_none():
	print "I got nothing"
	

print_two("Rasendran","Kirushan")
print_two_again("Rasendran","Kirushan")

print_one("Kirushan")
print_none()