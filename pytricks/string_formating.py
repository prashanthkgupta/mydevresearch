errno = 50159747054
name = 'Bob'

s = 'Hey ' + name + ', there is a ' + hex(errno) + ' error! '
print(s)

# old style
s = 'hey %s' % name
print(s)
s = 'Hey %s, there is a 0x%x error! ' % (name, errno)  # operator % takes only one argument
print(s)
s = 'Hey %(name)s, there is a 0x%(errno)x error! ' % {'name': name, 'errno': errno}
print(s)

# new style
s = 'Hey {}, there is a {} error! '.format(name, hex(errno))
print(s)
s = 'Hey {name}, there is a 0x{errno:x} error! '.format(name=name, errno=errno)
print(s)

# 3.6+
s = f'Hey {name}, there is a {errno:#x} error! '
print(s)


def greet(name, question):
    return f'hey {name}, how"s is everything {question}??'


print(greet('prashant', 'going'))
import dis
# dis.dis(greet)

# template string - best uses for user input string
from string import Template

t = Template('Hey $name, there is a $errno error! ')
print(t.substitute(name=name, errno=hex(errno)))

SECRET = 'my secret'


class Error:
    def __init__(self):
        pass


err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))
