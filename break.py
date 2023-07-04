prompt ="\nPLease enter the name of the city you have visited:"
prompt+="\n (Enter 'quit' when you are finished.)"

while True:
    city=input(prompt)
    if city =='quit':
        break
    else:
        print("I'd love to go to"+city.title()+"!")
        
# Using continue in a loop
# Rather than breaking out of a loop entirely without executing the rest of its
# code, you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test.

current_number=0
while current_number< 10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)


#Different ways of using the input function
 
name=input("\nTell me your name")
prom=("\nTell me more about yourself")
name2= input(prom)
# Using a while loop with lists and dictionaries
# Moving items from one list to another

# start with users that need to be verified
# and an empty list to hold confirmed users.
unconfirmed_users=['alice','brian','candance']
confirmed_users=[]
# verify each user until there are no more uncofirmed users
# move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print ("verifying user:"+current_user.title())
    confirmed_users.append(current_user)
    
# dispalying all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# Removing all instances of specific values from a list
pets=['cat','dog','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# Filling a dictionary with user input
responses={}

# set a flag to indicate that polling is active.
polling_active=True
name = input("\nWhat is your name?")
response=input("which mountain would you like to climb someday?")

# store the response in the dictionary:
responses[name]=response

# Find out if anyone else is going to take the poll.
repeat=input("Would you like to let another person respond?(yes/no)")
if repeat =='no':
    polling_active=False
    
# polling is complete.show the results.
print("\n---Poll Results---")
for name,response in responses.items():
    print(name+"would like to climb"+response+".")