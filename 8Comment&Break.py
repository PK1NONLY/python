Number = 26

# ok this program find a  number

'''
multiple comment
print("parshnat" + "pandit")
'''

for n in range(101):
    if n is Number:
        print(n, "is the number ! ")
        break
    else:
        print(n)

#Find the numbers whıch can dive 4 and 4 multiple(tetragenous) in from 0 to 100
for n in range(101):
    if n % 4 is 0:
        print(n)
