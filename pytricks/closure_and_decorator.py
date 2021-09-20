# closure function
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()

# decorator
# takes function as parameter, add some functionality then returns original function
def display_info(func):
    def inner(msg):
        print('Executing', func.__name__)
        func(msg)
        print('done executing')

    return inner


@display_info
def printer(msg):
    print(msg)


printer('Hello Sir')


def smart_devide(function):
    def inner(a, b):
        if b == 0:
            print('provide correct dividor')
        else:
            return a / b

    return inner


@smart_devide
def devide(a, b):
    return a / b


print(devide(5, 7))


def star(function):
    def inner():
        print('*' * 30)
        function()
        print('*' * 30)

    return inner


def devision(function):
    def inner():
        print('%' * 30)
        function()
        print('%' * 30)

    return inner


@devision
@star
def printt():
    print('Decorators are Awesome!!')


printt()
