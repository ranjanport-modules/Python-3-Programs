fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
split = []
fsplit = []
for line in fh:
    if  line.startswith("From"):
    	split=line.split()
    	count = count + 1
    	#print (split[1])

for s in split[1]:
	if s in fsplit:
		continue
	else:
		fsplit.append(s)
print(fsplit)
print("There were", count, "lines in the file with From as the first word")
