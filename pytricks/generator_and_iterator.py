# implementing iterator
class Even:
    def __init__(self, max):
        self.max = max
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


numbers = Even(10)
# print(next(numbers), 'from next')
# for n in numbers:
#     print(n)


# implementing iterator with generator
def generate_even(max):
    n = 2
    while n <= max:
        yield n
        n += 2


# generator expression
li = [1, 2, 3, 4]
li_sqr_generator = (x * x for x in li)
print(next(li_sqr_generator), 'from generator')
print(next(li_sqr_generator), 'from generator')

numbers = Even(10)
print(next(numbers), 'from next')
for n in numbers:
    print(n)


def generate_fibbonaci():
    a = 0
    b = 1
    yield a

    while True:
        a, b = b, a + b
        yield a


fic = generate_fibbonaci()
