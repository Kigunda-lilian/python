# Defining a function

def greet_user():
    """Display a simple greeting"""
    print("Hello!")
greet_user()

# passing information to a function
def greet_user2(username):
    print("Hello,"+username.title()+"!")
greet_user2("Lilian")

# Arguments and parameters
# Passing arguments- you can pass positional argumennts,keyword arguments , lists and dictionaries

# Positional arguments
def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='Hamster',pet_name='harry')
describe_pet('Dog','Chessy')

# Keyword arguments
# Default values-when writing a function you can define default values for each parameter
# note: default values are listed after non-default values
def describe_pet2(pet_name1,animaltype1='dog'):
    print(animaltype1 +" "+ pet_name1)
describe_pet2("willie")
describe_pet2("cat","fess")
describe_pet2(pet_name1="fess",animaltype1="cat")

# Equivalent function calls
# Avoiding argument errors