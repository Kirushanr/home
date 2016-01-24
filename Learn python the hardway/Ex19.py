def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get A Blankent \n"

print "We just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variable from our script:"
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can do math inside the functions too"
cheese_and_crackers(10+20,65+6);


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

