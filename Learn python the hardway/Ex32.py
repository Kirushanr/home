the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change =[1,'pennies',2,'dimes',3,'quaters']


# this first kind of for-loop goes through a list


for number in the_count :
	print "This is the count %d" % number

	
#same as the above
for fruit in fruits :
	print "A fruit of type: %s" %fruit 
	

#also we can go throuh mixed lists too
#notice we have to use %r since wer dont know 
#what's in it 


for i in change :
	print "I got %r" % i

	
#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range (0,6):
	print "Adding %d to the list" % i 
	elements.append(i)

	
#now we can print them out
for i in elements:
	print "Element was %d" % i
	
