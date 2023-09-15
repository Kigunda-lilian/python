# while loop to count from 1 to 5
i = 0
while i <= 5:
    print(i)
    i +=1
    
# prompt ="\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#          print (message)
         
current_number =0
while current_number <= 10:
    current_number+=1
    if current_number%2 == 0:
        continue
    print(current_number)

# A function that returns a dictionary
def attendees(first_name,last_name,middle_name = ""):
    if middle_name:
        person ={"first":first_name,"last":last_name,"middle":middle_name}
    else:
        person = {"first":first_name,"last":last_name}
        return person
    
attendee1 =attendees("lilian","kigunda")
print(attendee1)

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person

  
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def greet_user(names):
    for name in names:
        msg  = "Hello, " + name.title()
        print (msg)
        
usernames = ("nashlil","lilian","Moreen","Faith","Flora")
greet_user(usernames)

unprinted_designs = ["robot pendant","Iphone case","dodecahendron"]
completed_designs=[]

while unprinted_designs:
    new_design = unprinted_designs.pop()
    print("printing:"+new_design.title())

completed_designs.append(new_design)
print("The following models have been printed:")

for completed_design in completed_designs:
    print(completed_design)


# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)



completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
def print_models(unprinted_designs, completed_models):

 while unprinted_designs:
    current_design = unprinted_designs.pop()
    

# Simulate creating a 3D print from the design.
print("Printing model: " + current_design)
completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)




unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Passing an Arbitrary Number of Arguments
def pizza(*toppings):
    print(toppings)
    
pizza("mushroom","pineapple","extra cheese","pepperoni")

# The asterisk in the parameter name *toppings tells Python to make an
# empty tuple called toppings and pack whatever values it receives into this
# tuple.


# CLASSES
class Dog:
    def __init__(self,name,age):
     self.name = name
     self.age = age

#  A function that is part of a class is a method
    def sit(self):
     print(self.name.title() + " is now sitting.")

    def roll_over(self):
     print(self.name.title() + " rolled over!")
  
# Making an Instance from a Class
my_dog = Dog("Willie",6)
# Accessing Attributes
# To access the attributes of an instance, you use dot notation
print("My dog's name is " + my_dog.name.title())
print("My dog's age  is " + str(my_dog.age))
# Calling Methods
# After we create an instance from the class Dog , we can use dot notation to
# call any method defined in Dog .
my_dog.sit()
my_dog.roll_over()

# Modifying Attribute Values
# You can change an attribute’s value in three ways: you can change the value
# directly through an instance, set the value through a method, or increment
# the value (add a certain amount to it) through a method.


# INHERITANCE
# The first task Python has when creating an instance from a child class is to
# assign values to all attributes in the parent class. To do this, the __init__()
# method for a child class needs help from its parent class.

# Let’s start by making a simple version of the ElectricCar class, which
# does everything the Car class does:

class Car():
    def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year
      self.odometer_reading = 0
      
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
      
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
# The name of the parent class must be included in parentheses in the definition of the child class.
# The __init__() method takes in the information required to make a Carinstance.
# The super() function is a special function that helps Python makeconnections between the parent and child class. 
# This line tells Python to call the __init__() method from ElectricCar ’s parent class, which gives an ElectricCar instance all the attributes of its parent class. 
# The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
# we make an instance of the ElectricCar class, and store it in my_tesla . 
# This line calls the __init__() method defined in ElectricCar ,which in turn tells Python to call the __init__() method defined in the par-ent class Car .
# We provide the arguments 'tesla' , 'model s' , and 2016 .

# Overriding Methods from the Parent Class
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class.