################################################
# Dictionary Default Values
#################################################
d = {1: 1}
d = d.get(1, 'default')

################################################
# Dictionary Default Values
#################################################
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items()))  # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
print(sorted(xs.items(), key=lambda x: x[1]))  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
import operator

print(sorted(xs.items(), key=operator.itemgetter(1)))  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# with lambda I can get more control on sorted key
print(sorted(xs.items(), key=lambda x: abs(x[1])))  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
print(sorted(xs.items(), key=lambda x: x[1], reverse=True))


################################################
# Emulating Switch/Case with with dicts
#################################################
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    elif operator == 'sub':
        return x - y


# can be re-written using dictionary
def dispatch_if_with_dict(operator, x, y):
    return {
        'add': lambda x, y: x + y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y,
        'sub': lambda x, y: x - y,
    }.get(operator, lambda: None)(x, y)


print(dispatch_if_with_dict('add', 2, 4))

################################################
# The Craziest Dict Expression in the West
#################################################
d = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print(d)
print(True == 1 == 1.0)  # True
print([True, False][True])


# keys with equal value and same has are evaluated as same in the dictionary

class AlwaysEqual:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)


print(AlwaysEqual() == AlwaysEqual())  # True
objects = [AlwaysEqual(), AlwaysEqual()]
print([hash(x) for x in objects])
print(hash(AlwaysEqual()), hash(AlwaysEqual()))  # why these hashes are same


class SameHash:
    def __hash__(self):
        return 1


objects = [SameHash(), SameHash()]
print([hash(x) for x in objects])


class SameHashAndEqual:
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return True


ll = [SameHashAndEqual(), SameHashAndEqual(), SameHashAndEqual()]
ddd = {x: x for x in ll}
print(ddd)
print()

################################################
# Dictionary Pretty Printing
#################################################
ys = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
ys['e'] = {1, 2, 3}
print(ys)
import json

# print(json.dumps(ys, indent=4, sort_keys=True))
import pprint

pprint.pprint(ys)

################################################
# So Many ways to merge dictionary
#################################################
ys = {'a': 4, 'c': 2}
xs = {'b': 3, 'd': 1, 'a': 7}
zs = {}
zs.update(xs)
zs.update(ys)
print(zs)

zs1 = dict(xs, **ys)
print(zs1)
zs2 = {**xs, **ys}  # dict are evaluated left to right
print(zs2)
