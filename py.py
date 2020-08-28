largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
    	break
    try:
        possible=int(num)
    except:
    	print ("Invalid input")
    if smallest is None:
    	smallest = possible
    elif possible < smallest:
    	smallest = possible
    elif largest is None:
    	largest = possible
    elif possible > largest:
    	largest= possible
print ("Maximum is",int(largest))
print ("Minimum is",int(smallest))