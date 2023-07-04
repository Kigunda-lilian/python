from shutil import make_archive


greeting="Hello"
name="Lilian"
print(greeting+","+"name")
# function calculate with two required and two optional named arguments which calculates and returns a result.
def calculate(addition_one,addition_two,exponent=1,factor=1):
    result=(addition_one+addition_two)**exponent*factor
    return result
calculate(2,3)
calculate(2,3, factor=1)
x=6
if x > 5:
    print("{} is greater than five".format(x))
elif x < 0:   
    print("{} is negative".format(x))
else:
    print("{} is between zero and five".format (x))
  
y=[7890,45,67] 
for items in y:
    print (items)

while x < 15:
    x+=1     
    
    # python crash course practice questions
    #methods of printing a variable
name='Eric'
int_required=90
# method 1:Use comma(,) to separate variables and print them
print ("Hello,",name,",would you like to learn some python today?")
print("Hello,",name)
# method 2: use the string formattiing with the help of %
# The % sign, followed by a letter, works as a placeholder for the variable.
# For example, %d can be used as a placeholder when we need to substitute numerical values.
print("Hello to the  %s " %(name))
print("Hello %s at %d!" %(name,int_required))
# method 3: use the string formattiing with the help of {}
# When using string formatting, we can use {} to mark the place in the statement where the variable needs to be substituted.
print("Hello{} at {}!".format(name,int_required))
# method 4:Use the + Operator to Separate Variables in the print Statement
# This method can only concatenate strings not integers


print("Hello" +" "+name+" "+ "at" +" "+str(int_required))
var1= 123
var2= 'World'
print('Hello to the' + ' ' + var2 + " "+str(var1))
language = "Python"

#Adding the language variable into a string
print("Hello" +" "+ language +" "+ "World!")
# method 5:Use the f-string in the print Statement
# The f-string is another method of achieving string formatting 
var1= 123
var2= 'World'
print(f'Hello to the {var2} {var1}')
# even numbers between 0-13 using while loop
j = 0
while j <= 13 :
    print (j)
    j+=2
# printing a variable in lowercase,uppercase and titlecase
print(name.upper())
print(name.lower())
print(name.title())

# quotes in a string
quote="Albert Einsten once said,'A person who never made a mistake never tried anything new.'"
print(quote)
famous_person ="Albert"
message= famous_person,"once said,'A person who never made a mistake never tried anything new.'"
print(message)
message2="{} once said,'A person who never made a mistake never tried anything new2.'".format(famous_person)
print(message2)
message3="%s once said,'A person who never made a mistake never tried anything new3.'"%(famous_person)
print(message3)
# tabs and new line
name1="\tLilian\nKanana"
print(name1)
# removing white spaces
name2 = "   Alfred Juma   "
print(name2)
print(name2.strip())
print(name2.rstrip())
print(name2.lstrip())
import this
friends=["wed","sat","fri"]
print(friends[0].upper())
print("Hello {} juma".format(friends[0]))
del friends[1]
print (friends)
popped_friends=friends.pop()
print(friends)
print(popped_friends)
friends.append("lil")
friends.insert(2,"nash")
print(friends)
friends.pop(1)
print(friends)
# removing an item by value
mortocycles=["honda","yamaha","suzuki","ducati"]
mortocycles.remove("ducati")
print(mortocycles)
# organizing a list
# Sorting a List Permanently with the sort() Method
cars=["bmw","audi","toyota","subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# Sorting a List Temporarily with the sorted() Function
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function
days=["Monday","Tuesday","Wednesday","Thursday","Sunday"]
print("\nHere is the sorted list:")
print(sorted(days))
print(days)
print (cars)
days.reverse()
print(days)
len(days)
# for loop
# Any lines of code after the for loop that are not indented are executed once without repetition.
universities=['Meru university','Egerton','Embu','UOE','UON']
for university in universities:
    print(university)
    print(university.upper()+", is my school!")
    print("You should visit my school\n")
print("They are all good schools!")
# using range function
for value in range(1,13):
    print(value)
    value+=2
    
numbers = list(range(1,6))
print(numbers)

# printing even numbers
even_numbers=list(range(2,11,2))
print(even_numbers)

for even in range(2,20,2):
    print(even)

# a list of the first 10 square numbers (that is, the square of each integer from 1 through 10).

# method 1
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
# method 2
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

# List Comprehensions
# building the squares of numbers using list comprehension
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
squares = [value**2 for value in range(1,11)]
print(squares)

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.upper())

print(players[1:4])
    
numbers=[1,2,23,67,87,78,90,12,4,32,1]
numbers.sort(reverse=True)
print (numbers)

# copying a list
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ( [:] ). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]
print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_food)

# Tuples- list of items that can not change
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# A tuple looks just like a list except you use parentheses instead of square brackets.
dimension=(30,67)

# IF STATEMENTS
Cars=["Audi",'bmw','subaru','toyota']
for car in cars:
    if car =='audi':
     print(car.upper())
    else:
     print(car.title())
     
     
# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
            print(user.title() + ", you can post a response if you wish.")

age=12
if age <4:
    print('your admission cost is $0')
elif age <18:
    print('your admission cost is $5')
else:
    print('your admission cost $10')


age=20
if age <4:
    price=0
elif age <18:
    price=5
else:
    price =10
print('your admission cost is $'+str(price)+".")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']  
for requested_topping in requested_toppings:
    print("\nAdding " + requested_topping + ".")
print("\nFinished making your pizza!")

# if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']  
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we are out of green peppers for now")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print('\n Finished making your pizza!')

# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")
    
# DICTIONARIES-a collection of key-value pairs
# A key-value pair is a set of values associated with each other
# A dictionary is similar to a list, but it allows you to connect pieces of information.
# building dictionaries, looping through them, and using them in combination with lists and if statements.
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
# storing different kinds of information about one object,
alien_0 = {'color': 'green', 'points': 5}
# Accessing Values in a Dictionary
# To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
print(alien_0['color'])
print(alien_0['points'])

color=['green','yellow','pink']
print(color[1])

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
    
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
    
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment


print("New x-position: " + str(alien_0['x_position']))

# Removing key-value pairs
# Use the del statement
# All del needs is the name of the dictionary and the key that you want to remove.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# A dictionary of similar objects
# Storing one kind of information about many objects.


# When you know you’ll need more than one line to define a dictionary, press enter after the opening brace. Then indent the next line one level (four spaces), and write the first key-value pair, followed by a comma. 

# From this point forward when you press enter , your text editor should automatically indent all subsequent key-value pairs to match the first key-value pair.

# Once you’ve finished defining the dictionary, add a closing brace on a new line after the last key-value pair and indent it one level so it aligns withthe keys in the dictionary.
 
# It’s good practice to include a comma after thelast key-value pair as well, so you’re ready to add a new key-value pair on the next line

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print(favorite_languages)

# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
user_1={
    'username':'kanana',
    'first':'lilian',
    'last':'Kigunda',
    }
for key,value in user_1.items():
    print("\nkey:"+key)
    print("value:"+value)
    
# Looping Through All the Keys in a Dictionary
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in favorite_languages.keys():
    print(name.title())
    
    
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
friends = ['phil', 'edward']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print("hello"+name.title()+' '+'I see your favourite language is'+' '+favorite_languages[name].title()+"!")
        
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
if 'erin' not in favorite_languages.keys():
    print('Erin,please take your poll!')


# Looping Through a Dictionary’s Keys in Order
# # One way to return items in a certain order is to sort the keys as they’rereturned in the for loop. You can use the sorted() function to get a copy of
# the keys in order:
# his for statement is like other for statements except that we’ve wrapped the sorted() function around the dictionary.keys() method.

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
# Looping Through All Values in a Dictionary
# If you are primarily interested in the values that a dictionary contains,you can use the values() method to return a list of values without any keys.

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# To see each language chosen without repetition, we can use a set.
# A set is similar to a list except that each item in the set must be unique:
# When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items.
#The result is a nonrepetitive list of languages that have been mentioned by people taking the poll: 
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for language in set(favorite_languages.values()):
    print(language.title() )
    
# Nesting
# Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. This is called nesting.
# You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even adictionary inside another dictionary.

# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens=[]

# make 30 green aliens
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
# show the first five aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print("Total number of aliens:"+str(len(aliens)))

# Make an empty list for storing aliens.
aliens=[]

# make 30 green aliens
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
    for alien in aliens[0:3]:
        if alien['color']=='green':
            alien['color']='yellow'
            alien['speed']='medium'
            alien['points']=10
# show the first five aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# A list in a dictionary
# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
# Inside the dictionary’s for loop, we use another for loop to run through the list of languages associated with each person:

favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    print('\n'+name.title()+"'s fovourite languages are:")
    for language in languages:
        print("\t"+language.title())
        
# to do:To refine this program even further, you could include an if statement at the beginning of the dictionary’s for loop to see whether each person has more than one favorite language by examining the value of len(languages) .
# If a person has more than one favorite, the output would stay the same.
# If the person has only one favorite language, you could change the wording to reflect that. For example, you could say Sarah's favorite language is C .


# A dictionary in a dictionary
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername:"+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    
    print("\tFull name:"+full_name.title())
    print("\t Location:"+location.title())
    
# User inputs and while loop
message= input("Tell me something and I will repeat it back to you:")
print(message)

name= input("Please enter your name: ")
print("Hello," + name+"!" )

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input (prompt)
print ("\n Hello,"+name+"!")


# Using int() to Accept Numerical Input
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number =input("Enter a number, and I'll tell you if it's even or odd")
number = int(number)
if number % 2 ==0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
    
current_number = 1
while current_number <= 5:
    print (current_number)
    current_number+=1
    
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message!='quit':
    message = input(prompt)
    print(message)
    
# Using a Flag
# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire pro-gram is active. This variable, called a flag, acts as a signal to the program.

# We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False . 
# As a result,our overall while statement needs to check only one condition: whether or not the flag is currently True . Then, all our other tests (to see if an event has occurred that should set the flag to False ) can be neatly organized in the rest of the program.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active=True
while active:
    message = input(prompt)
    if message == 'quit':
        active=False
    else:
        print (message)
        
        
# Using break to Exit a Loop
# Use the break statement
# you can use it to control which lines of code are executed and which aren’t, so the program only 
# executes code that you want it to, when you want it to