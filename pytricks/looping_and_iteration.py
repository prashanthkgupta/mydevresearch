######################################################
# Writing Pythonic Loops
######################################################
l = [1, 2, 3, 4]

for e in l:
    print(e)

for i, e in enumerate(l):
    print(i, e)

for i in range(0, 10, 2):
    print(i)

######################################################
# Comprehending Comprehensions
######################################################
l = [x * x for x in range(10) if x % 2 == 0]
s = {x * x for x in range(10) if x % 2 == 0}
d = {x: x * x for x in range(10) if x % 2 == 0}
print(d)

l = [x * x if x % 2 == 0 else x * x * x for x in range(10)]
print(l)

######################################################
# List Slicing and Shushi Operator
######################################################
# [start, end, step]
s = list('prashant')
print(s[-1::-1])  # reverse a string or s[::-1])
del s[:]  # deletes all the elements of a list
s.clear()  # also deletes all the elements from a list
s[:] = [1, 2, 3]
print(s)


######################################################
# Beautiful Iterators
######################################################
# for each is supported for every class that implements __next__ and __iter__ dunder methods

class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


# repeater = Repeater('Hello')
# for i in repeater:
#     print(i)

# above three lines can be re-written
repeater = Repeater('Hello')
iterator = repeater.__iter__()


# while True:
#     item = iterator.__next__()
#     print(item)


class BoundRepeater:
    bound = 5

    def __init__(self, value, bound=5):
        self.value = value
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.bound:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundRepeater('Hello')
iterator = repeater.__iter__()


# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         pass
######################################################
# Generators are simplified iterators - yield
######################################################
def repeater(value):
    while True:
        yield value


re = repeater('hello')
print(re)  # <generator object repeater at 0x7f539e02d518>
######################################################
# Generators Expressions
######################################################
# ge cant be restarted or reused
ge = ('hello' if i > 1 else 'bye' for i in range(3))
print(ge)  # <generator object <genexpr> at 0x7f2ef0637518>
for e in ge:
    print(e)
print(sum(i for i in range(10)))  # even () can be dropped in case of inline generator expression


# more than two levels of generators are not recommended


######################################################
# Iterators Chains
######################################################
# for data pipelines
def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for e in seq:
        yield e * e


def negated(seq):
    for e in seq:
        yield -e


print(negated(squared(integers())))

x = negated(squared(integers()))
print(x.__next__())
print(x.__next__())
print(x.__next__())
