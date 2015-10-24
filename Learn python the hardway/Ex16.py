from sys import argv

script,filename= argv

print "We're going to erase the %r" % filename
print "If you don't won't that hit CTRL+C"
print "If you do want that hit return"

raw_input("?")
print "Opening the file"
target=open(file,"w")

print "Truncating the file Goodbye!!!"

#Delete contents of the file
target.truncate()


print "Now i'm going to ask you three lines"

line1=raw_input("Line 1: ")
line2=raw_input("Line 2: ")
line3=raw_input("Line 3: ")

print "I'm going to print the lines";

target.write(line1);
target.write(line2);
target.write(line3);
target.write(line4);


target.read();
