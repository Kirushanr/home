
from sys import argv
from os.path import exists


#passing command line parametes 
#First Parameter script denotes the script name 
#from_file denotes from which file 
#Which file we're copying the content

script , from_file , to_file = argv
print "Copying from %s to %s" % (from_file , to_file)


#we could do those to on one line too
indata=open(from_file).read()

print "The input file is %d bytes long" % len(indata)

#check if the file exists 
print "Does the output file exist %r" % exists(to_file);


print "Ready, hot return to continue CTRL-C to abort"

raw_input()

#open the file with write permission
out_file=open(to_file,'w')
#writing the content to the 
out_file.write(indata);

print "Allright , all done. "

#close the file object this returns true when closed successfully
out_file.close()
