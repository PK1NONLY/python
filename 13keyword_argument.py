def dumb_sentence(name='parshant', action='ate', item='jalebi'):
    print(name, action, item)

dumb_sentence()
dumb_sentence("raj", "went", "gently")
dumb_sentence(item='samosa')
dumb_sentence(item='awesome', action='is')


# flexible arguments
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 43, 5453, 354234, 463463)


# unpacking argument

def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate*3.5) - (cigs_smoked*2)
    print(answer)

my_data = [27, 20, 0]

health_calculator(my_data[0], my_data[1], my_data[2])
health_calculator(*my_data)