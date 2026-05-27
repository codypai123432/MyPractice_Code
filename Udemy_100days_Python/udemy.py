
# Entering Name and ask python not to forget you have to make define your variable 
number = int(input('what is your age:'))
if number < 2:
 print('you are a baby')
else:
 print ('Old Enough')
 pass



name = input("what is your name")  
print(f"Hello {name}")
print("Hello "+ name)
pass



# have to define variables if you have multiple value in input arrary, then python wouldnt skip (not skip but due to tuple comparision math) the rest once it found the first arrey value does not fit the condition. 
red= int(input("Enter Red Vaule:"))
green= int(input("Enter green Vaule:"))
blue= int(input("Enter blue Vaule:"))
pass

colorcode =(red,green,blue)
pass

if colorcode < (0,0,255):
 print("it might be blue")
else:
 print("it is not blue")
pass

# Another example if you only want to see if it is blue or not, we can focus on the vaule blue

red = int(input("Red:"))
green = int(input("Green:"))
blue = int(input("blue:"))
pass

if blue > 150 and red < 50:
  print("It might be blue")
pass

name_len = len(input("What is your name:"))
print (name_len)

age = int(input("What is your age: "))
print(age)
