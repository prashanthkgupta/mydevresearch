class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello1.txt') as f:
    f.write('Hello World!!')
    f.write('Bye Now!!')

# with context manager
from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f1 = open(name, 'w')
        yield f1
    finally:
        f1.close()


with managed_file('hello.txt') as f:
    f.write('Hello World!!')
    f.write('Bye Now!!')


# indenter using class
class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level, text)


# with Indenter() as indent:
#     indent.print('hi')
#     with indent:
#         indent.print('hello')
#         with indent:
#             indent.print('bonjour')
#     indent.print('hello bro')

level = 0


def printt(text):
    print(' ' * level, text)


@contextmanager
def indentor():
    global level
    level += 1
    yield
    level -= 1


with indentor():
    printt('hi')
    with indentor():
        printt('hello')
        with indentor():
            printt('bonjour')
    printt('hello bro')

# execution time using context manager
import time


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start_time)


# with ExecutionTime() as et:
#     time.sleep(5)


@contextmanager
def execution_time():
    start_time = time.time()
    yield
    print(time.time() - start_time)

with execution_time() as et:
    time.sleep(3)


