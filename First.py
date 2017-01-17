print('first command')

print ('------------------------')

x = 3+5
print (x)
print ('------------------------')

foods = ['bacon', 'tuna', 'ham', 'snausages', 'beef']

for f in foods[:2]:
    print(f)
    print(len(f))
print ('------------------------')

age = 21
if age < 21:
    print ('you are not eligible')
elif age > 21:
    print('eligible')
else:
    print ('you are 21')
print ('------------------------')

name = "Raj"
if name is "pkay":
    print("Hii! Pkay")
elif name is "Lucky":
    print("What up lucky")
elif name is "raju":
    print("What up raju")
else:
    print("Please sign up for the site!")
print ('------------------------')

for x in range(10):
    print(x)
print ('------------------------')

for x in range(5, 12):
    print(x)
print ('------------------------')

for x in range(10, 40, 5):
    print(x)

print ('------------------------')

y = 5

while y < 10:
    print(y)
    y += 1

print ('-----------------------')

magicNumber = 26

# sigle line comment

'''
multiple comment
print("abc" + "xyz")
'''

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number ! ")
        break
    else:
        print(n)
print ('-----------------------')

for f in range(101):
    if f % 4 is 0:
        print (f)
print ('-----------------------')

number = [2, 5, 7, 9, 14, 17, 19]
for n in range(1, 20):
    if n in number:
        continue
    print(n)
print ('-----------------------')


def function():
    print('this is a function')
function()
print ('-----------------------')


def square(number):
    result = number*number
    print(result)
square(15)
square(5)
square(25)
square(65)
print ('-----------------------')


def result(num):
    result = num*(num+1)
    return result
result5 = result(5)
result2 = result(2)
result3 = result(3)
print(result5)
print(result2)
print(result3)
print ('-----------------------')


def chekgender(gender='unknown'):
    if gender is 'm':
        gender = 'male'
    elif gender is 'f':
        gender = 'female'
    print(gender)
chekgender('m')
chekgender('f')
chekgender()

print ('-----------------------')


a = 7823


def fun():

    print(a)


def fun2():
    print(a)


fun()
fun2()
print ('-----------------------')

#Keyword argument
def thisfunction(name='pkay', action='cooks', object='samosa'):
    print (name, action, object)


thisfunction()
thisfunction("anil", "sings", "song")
thisfunction(object="biryani")
thisfunction(object="mango", action="eats")
print ('-----------------------')

#Flexible argument

def addition(*args):
    sum = 0
    for a in args:
        sum += a
    print (sum)
addition(5)
addition(5, 3, 34, 5, 6, 6, 7, 7,)
addition(5, 45, 67897, 8934)
print ('-----------------------')

#unpacking argument
def required_runrate(target, score, remainingOver):
    requiredrunrate = (target - score) / remainingOver
    print(requiredrunrate)
score_card=[350, 250, 15]
required_runrate(score_card[0], score_card[1], score_card[2])
required_runrate(*score_card)

#sets

items = {'books', 'pen','shoes',',milk','tea','pen'}

print(items)
if 'pen' in items:
    print('you already have pen in items')
else:
    print('no! you do not have pen in your items.')