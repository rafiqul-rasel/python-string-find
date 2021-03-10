filename = "l.txt"

#Open the file
infile = open(filename, 'r') 

lines = infile.readlines() 
f = open("lo.txt", "a")


for line in lines:
	sline = line.split(' ')  # separates line into a list of items.  ',' tells it to split the lines at the commas
	#print(sline[0]) #each line is now a list
	f.write(sline[0])
	f.write('\n')
f.close()
infile.close()