# this variable a can be used in any method or function
a = 7823


def function_a():
    # this variable b can be used only in this method
    b = 7657656
    print(a)
    print(b)


def function_b():
    print(a)
    # this next line will cause error coz variable b can only used inside function_b
    # print(b)

function_a()
function_b()
