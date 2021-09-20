import functools


def yell(text=''):
    return text.upper() + '!'


bark = yell
# del yell

print(bark('bhow'))
print(bark.__name__)  # yell

functions = [yell, bark, str.lower]
for f in functions:
    print(f, f('hello'))
# function can be passed to other function
# higher-order functions - take function as arguments like map
# hof are necessity for functional programming style
li = ['a', 'b', 'c']
upper_li = list(map(str.upper, li))
print(upper_li)


# function can be n nested
# function can capture local state
# lexical closure - A closure remembers the values from its
#   enclosing lexical scope even when the program flow is no longer on that scope
# objects can behave like functions using dunder __call__
class Adder:
    def __init__(self, n: int):
        self.n = n

    def __call__(self, x):
        return self.n + x


adder = Adder(5)
print(adder(3))

print(callable(adder))

######################################################
#      lambdas are single-expressions function       #
######################################################

add_ = lambda x, y: x + y
print(add_(5, 6))

print((lambda x, y: x + y)(3, 4))

# can be defined in one line only
# when I need to pas a function to another function then passing lambda will be better
#   bcz I don't need to assign a function name

tuples = [(1, 'd'), (4, 'c'), (2, 'b'), (3, 'a')]
print(sorted(tuples, key=lambda x: x[0]))

print(sorted(range(-5, 6), key=lambda x: x * x))


# lambda also works with lexical closure
def make_adder(n):
    return lambda x: x + n


plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_5(7))

# lambda, map and filter should be used sparingly

# Harmful
evens = list(filter(lambda x: x % 2 == 0, range(20)))
print(evens)
# better
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
evens = [x if x % 2 == 0 else x * x for x in range(20)]


######################################################
#      Power of decorators       #
######################################################
# decorators allows you to extend and modify the behaviour of a callable without modifying callable

def null_decorator(func):
    return func


def greet():
    print('Hello')


# decorating function manually if we don't want always to be decorated
greet_null_decorated = null_decorator(greet)
greet_null_decorated()


# sugar coated decoration
@null_decorator
def greet():
    print('Hello')


greet()


def star(function):
    @functools.wraps(function)
    def inner():
        print('*' * 30)
        function()
        print('*' * 30)

    return inner


def devision(function):
    @functools.wraps(function)
    def inner():
        print('%' * 30)
        function()
        print('%' * 30)

    return inner


# decorators are used from bottom to top
@devision
@star
def printt():
    '''this is print'''
    print('Decorators are Awesome!!')


# sometimes lots of decoration might create performance issue if we are working performance intensive code


print(printt.__name__)  # inner if @functools.wraps(function) not used else printt
print(printt.__doc__)  # None if @functools.wraps(function) not used else printt 'this is print'


######################################################
#      Fun with *args and **kwargs                   #
######################################################
def foo(required, *args, **kwargs):
    print(required, args, kwargs)
    foo_pass(required, *args, **kwargs)  # passing args and kwargs to other function


def foo_pass(required, *args, **kwargs):
    print(required, args, kwargs)


foo('hello', 1, a=1, b=2)


######################################################
#      Functional argument unpacking                 #
######################################################
def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')


li = [1, 2, 3]
t = (1, 2, 3)
d = {'x': 1, 'z': 3, 'y': 2}
print_vector(*li)
print_vector(*t)
print_vector(*d)  # keys will be passed
print_vector(**d)

######################################################
#      Nothing to Return Here                       #
######################################################
# procedure - when a function does not return anything print
# by default a function returns None
# but for better readability we might need to add return in non-procedural functions
