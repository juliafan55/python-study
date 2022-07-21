
# advanced python arguments

# *args
# unlimited arguments -> the asterisk says that it'll accept any kind/number of arguments
# also known as unlimited positional arguments

# def add(*args):
#     for n in args:
#         print(n)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(2, 4, 6, 8))

# *kwargs
# many keyworded arguments

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")  # will return none io error
        self.color = kw.get("color")


my_car = Car(make="Nissan")
print(my_car.model)
