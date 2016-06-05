from sys import argv

#pass the file name as commandline argument
script , filename=argv

#open the file and the file object stored 
#inside the variable txt
txt = open(filename)

print "Here is your file %r: " % filename

print txt.read()

#close the file after reading
txt.close();
print "Type the filename again: "
file_again=raw_input("> ")

#open the file and the file object stored 
#inside the variable
txt_again =open(file_again)
print txt_again.read()
