number = input('please enter any value: ')

try:
    print('your age',10 + int(number))

except:
    print('That is not a valid number!')


# Loop
for i in range(10):
    print('help', i + 1)


i = 3

while i < 5:
    i = i + 1
    print(i)


while True:
    number = input('Enter any number: ')

    def hello(name):
        print('Who the hell', name, int(number))

    hello('Cody')
    hello('Pai')

