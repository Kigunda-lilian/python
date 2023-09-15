x = 4
if x > 5 :
    print("{} is greater than five" .format(x))
elif x < 0 :  
    print(" {} is negative" .format(x))
else:
    print("{} is between zero and five" .format(x))
    
    
    
t = [2,3,4,5]
for num in t:
    print(num)

v =0
while v < 8:
    v +=1
    print (v)


x = 0
while x <=8:
    x+=1
    print (x)
    
famous_person ="Albert"
message2="{} once said,'A person who never made a mistake never tried anything new2.'".format(famous_person)
print(message2)

name1 = "\tlilian\nkanana\tkigunda"
print(name1)
name2 = "   Alfred Juma   "
print(name2)
print(name2.strip())
print(name2.rstrip())
print(name2.lstrip())

days =["wed","thur","fri"]
poppped = days.pop()
print (poppped)
days.append("sat")
print(days)

universities=['Meru university','Egerton','Embu','UOE','UON']
for university in universities:
    print(university)
    print(university.upper()+", is my school!")
    print("You should visit my school\n")
print("They are all good schools!")

u = 0
while u < 10:
    print(u)
    u+=2

# u =[0,1,2,3,4,5,6,7,8,9,10,11,12]
# for even in u:
    
for value in range (0,20) :
    print(value)
    value+=2   
    
# using range function
for value in range(1,13):
    print(value)

numbers = list(range(1,6))
print (numbers)

even_numbers =list(range(2,20,2))
print(even_numbers)

# a list of the first 10 square numbers (that is, the square of each integer from 1 through 10).
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.upper())
print(players[1:4])

numbers=[1,2,23,67,87,78,90,12,4,32,1]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)

Cars = ["Audi",'bmw','subaru','toyota']
Cars[0] = "mercedes"
print (Cars)

cars=["audi",'bmw','subaru','toyota']
for car in cars:
    if car =='audi':
     print(car.upper())
    else:
     print(car.title())
     
     
     
subjects = ["english","mathematics","science","Geography"]
for subject in subjects:
    if subject == "science":
        print(subject.upper())
    else:
        print(subject.title()) 
        

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
 
names = ("lilian","janet","raphael")
print(names[2])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0["color"])


# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['color'] = "yellow"
print(alien_0)

del alien_0['points']
print(alien_0)


user_1 ={
     'name: lilian',
     'school:jkuat',
     'home:meru',
}
print(user_1)



# Starting with an Empty Dictionary
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

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
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input (prompt)
print ("\n Hello,"+name+"!")





