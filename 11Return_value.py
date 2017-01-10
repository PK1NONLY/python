# basic function
def allowed_dating_age(my_age):
    girls_age = (my_age/2)+7
    return girls_age

my_limit = allowed_dating_age(22)
your_limit = allowed_dating_age(49)
print("i can date girls", my_limit, "or older")
print("you can date girls", your_limit, "or older")


# default return value
def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()
