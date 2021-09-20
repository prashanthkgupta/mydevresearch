######################################################
# Dictionary, Maps and Hashtable
######################################################
import dis

phonebook = {
    'prashant': 9889059224,
    'papa': 9651336527
}
print(phonebook['prashant'])

squares = {x: x * x for x in range(1, 11)}
print(squares)

# dictionary key can be only hashable objects - string, numbers, tuple (if only contains hashable)
# python 3.6+ remembers insertion of objects in the dictionary

from collections import OrderedDict

d = OrderedDict([('p', 1), ('a', 2)])
print(d['p'])

from collections import defaultdict

dd = defaultdict(list)
print(dd['as'])  # will return the default values

from collections import ChainMap

d = {1: 1, 2: 2}
d1 = {3: 3, 4: 4}
chain = ChainMap(d, d1)  # search in all dict but insertion, update and delete works on first dictionary
print(chain)

from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

writable['one'] = 12  # read_only gets reflected if writable changes
print(read_only)

######################################################
# Array, Data Structures
######################################################
# list - dynamic array
l = [1, 2, 3, 'hello']  # will take more space from type coupled data structures
del l[1]
# tuple - immutable,
t = 1, 2, 3
print(t)  # (1, 2, 3)
print(t + (4,))

#  array.array - dynamic typed array, memory efficient than list and tuple
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])
arr.append(1)
print(arr)

# str - Immutable arrays of Unicode characters
arr = 'abcd'
print(arr[0])
l_s = list(arr)
s = ''.join(l_s)
print(s)
# str are recursive data structure
print(type(s))  # <class 'str'>
print(type(s[1]))  # <class 'str'>

# bytes - Immutable bytes of Single Bytes (0-255)
arr = bytes((0, 1, 3, 2))
print(arr)  # b'\x00\x01\x03\x02'
print(arr[0])
arr = bytes((0, 1, 3, 255))

# bytearray - Immutable bytes of Single Bytes (0-255)
arr = bytearray((0, 1, 3, 2))
arr[1] = 12
print(arr[1])

# str are recursive data structure


######################################################
# Records, Structs and Data Transfer Objects
######################################################
print(dis.dis(compile("[1,2,3,4]", '', 'eval')))
# dict
# tuples
# writing a custom class: more work, more control
# collections.namedtuple
# typing.namedtuples 3.6+
from typing import NamedTuple  # immutable


class Car(NamedTuple):
    color: str  # not forced just a suggestion for better documentation
    mileage: float
    automatic: bool


# struct.struct - Serialized C Structs
# can be used to handle binary data stored in files or coming in network connections
from struct import Struct

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
print(MyStruct.unpack(data))  # (23, False, 42.0)

# types.SimpleNamespace - Fancy Attribute Access
from types import SimpleNamespace

car1 = SimpleNamespace(color='red', mileage=3812, automatic=True)
print(car1.color)
del car1.color
car1.b1 = 'as'
print(car1)  # namespace(automatic=True, b1='as', mileage=3812)

######################################################
# Sets and Multi Sets
######################################################
s = {'a', 'e', 'i', 'o', 'u'}
s1 = {x for x in range(10)}
print(s)
## set
s2 = set()  # empty set
# any hashable object can be stored in set
s2.add(1)
print(s2.intersection(s1))

## frozenset - immutable sets
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
print(vowels)

# collections.Counter - Multisets (allows elements to be present more than once
from collections import Counter

inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)  # Counter({'bread': 3, 'sword': 1})
inventory.update({'sword': 1, 'apple': 1})
print(inventory)  # Counter({'bread': 3, 'sword': 2, 'apple': 1})
print(len(inventory))  # 3
print(sum(inventory.values()))  # 6

######################################################
# Stacks
######################################################
# list
s = []
s.append(1)
s.pop()

# collections.deque - implemented using doubly linked list
from collections import deque

s = deque()
s.append(1)
s.pop()

# queue.LifoQueue - Locking semantic for parallel computing
# synchronised and provides locking to support multiple concurrent producers and consumers
from queue import LifoQueue

s = LifoQueue()
s.put('a')
s.get()

######################################################
# Queues
######################################################
# list - terribly slow
q = []
q.append(1)
q.pop(0)

# collections.deque - implemented using doubly linked list
from collections import deque

s = deque()
s.append(1)
s.popleft()

# queue.Queue - Locking semantics for parallel Computing
# synchronised and provides locking to support multiple concurrent producers and consumers
from queue import Queue

q = Queue()
q.put(1)
q.get()
# print(q.get_nowait())


# multiprocessing.Queue - Shared job queues
from multiprocessing import Queue

q = Queue()
q.put(1)
q.get()

######################################################
# Priority Queues
######################################################
# heapq - List Based Binary Heaps - insertion and extraction takes o(logn)
# only min heap property
import heapq

q = []
heapq.heappush(q, (211, 'code'))
heapq.heappush(q, (23111, 'code'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# queue.PriorityQueue - Beautiful priority queues
# uses heapq but synchronised
from queue import PriorityQueue

q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while q:
    next_item = q.get()
    print(next_item)
