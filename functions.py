'''

def hello_func(greeting, name = "You"):
    return "{}, {}".format(greeting, name)

print(hello_func("Hi", name = "Cory"))


def student_info(*args, ** kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]
info = {"Name": "John", "Age": 25}

student_info(*courses, **info)

'''

# from modules import find_index, test
# import sys

# courses = ["History", "Math", "Physics", "Compsci"]

# index = find_index(courses, "Math")
# # print(index)
# # print(test)

# print(sys.path)

# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))

# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="Adonis", age=24)


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return(input)


print(fizz_buzz(7))

