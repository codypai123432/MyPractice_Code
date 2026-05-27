
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


# Data Type Transfer

integer = 20
name ='Cody'
skill_level = 30
string_number = '23'

print('The total skill:',(10+int(string_number)+ int(skill_level))) #tranforming the data type for handling multiple data units



#Math

addition = 32+20
FloorDivision = 32//3
Modulo=32%3
print(FloorDivision)
print(Modulo)


# if or conditional operation (logic) Two Types

age = 2
isHappy = True

if age > 21:
    print('You are old')
elif age ==18:
    print('You are getting old')
else: 
    print('You are still young')

   
if isHappy:
    print('Have a nice day bud!')
else:
    print('Come on! You are the best!')


# the for loop 
for i in range (10):
    print('Hello', i + 1)

print(range(3))

name_list = ['Luigi','Mario','Toad'] #can print the name list

for name in name_list:
    print(name)



data_list = ['23', '40', '80']  # experimenting data list printing

for data in data_list:
    print(data)



# The while loop 
i=2
while i<5:
    i=i+1
    print(i)

while True:
    user_input = input('Enter something >>')
    if user_input == '0':
        print('We are done here.')
      
    pass 

def say_hello(name,age):
    print('Hey there', name, age)

say_hello('Mario','20')
say_hello('Luigi','13')