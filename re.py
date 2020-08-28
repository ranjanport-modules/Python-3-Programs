#  print series like
#1 2 3
#2 4 6
#3 6 9
def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above




#3     count digits in the number
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n>0):
		count += 1
		n=n // 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1



#2  print word letter in lines
def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter


# print Number table
number = 1
while number <= 7:
	print(number, end=" ")
	number+=1



# countdown and count Up
	def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x>stop:
				return_string += ","
			x = x-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x+1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

#The even_numbers function returns a space-separated string of all
# positive numbers that are divisible by 2,
# up to and including the maximum that's passed into the function. 
#For example, even_numbers(6) returns “2 4 6”.
def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1,2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed



#palindrome String Check
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	input_string =  input_string.lower()
	# Traverse through each letter of the input string
	for k in input_string:
		if k!=" ":
			new_string =new_string+ k
			reverse_string = k+reverse_string

	# Compare the strings
	if new_string == reverse_string :
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


#Miles to KM
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km





#Print First name and 1st character of Last name
def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 




#The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
	listed = sentence.split() 
	if listed[-1] == old:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		listed[-1] = new
		emstring = " "
		new_sentence = emstring.join(listed)
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"



#Append using enumerate

def skip_elements(elements):
	# code goes here
	new = []
	i = 0
	for index,element in enumerate(elements):
		if  index==0:
			new.append(element)
		elif (index % 2) == 0: 
			new.append(element)
	return new

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


#Replace Extenssion in a list
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames =[]
newfilenames =[x.replace(".hpp",".h") for x in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#Let's create a function that turns text into pig latin: a simple text transformation that modifies
# each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
  say = " "
  pi = []
  # Separate the text into words
  words =  text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + 'ay'
    # Turn the list back into a phrase
    pi.append(word)
    pigged = say.join(pi)
  return pigged
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



#The group_list function accepts a group name and a
# list of members, and returns a string with the format: group_name: member1, member2, … 
#For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

def group_list(group, users):
  members = ", ".join(users)
  return "{}: {}".format(group,members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence
# "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
# ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. 
#Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

#The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
#Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).



def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+"@" + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))



#The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. 
#Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			# groups for this user, creating the entry
			# in the dictionary if necessary
			user_groups[user] = user_groups.get(user,[]) + [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


#The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for fruit, prices in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
			total += basket.get(fruit)
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44








#The format_address function separates out parts of the address string into new strings: house_number and street_name,
# and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the 
#street name which may contain numbers, but never by themselves, and could be several words long. For example
#, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".
# Fill in the gaps to complete this function.
def format_address(address_string):
  # Declare variables
  house_number = ""
  street_name = ""


  # Separate the address string into parts
  house_number , street_name = address_string.split(" ",1)
  

  # Return the formatted string  
  return "house number {} on street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"





#Short Form MAker

def initials(phrase):
	words = phrase.split()
	result = ""

	for word in words:
		result += word[0]
	return result.upper()


print(initials("Universal Serial Bus")) # Should be: USB










#Combine list by reversing first list

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  new_list = list2 + list1
  return new_list
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


#The City class has the following attributes: name, country (where the city is located), 
#elevation (measured in meters), and population (approximate, according to recent statistics). 
#Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma),
# when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million:
# max_elevation_city(1000000) should return "Sofia, Bulgaria".


# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	return_city = City()

	if city1.population >= min_population and city1.elevation > return_city.elevation:
		return_city =  city1
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3
	if return_city.name:
		return ("{},{}".format(return_city.name,return_city.country))
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""