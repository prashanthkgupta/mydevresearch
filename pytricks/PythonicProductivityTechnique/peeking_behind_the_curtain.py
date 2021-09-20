##############################################
#  Exploring Python Module and Objects
##############################################
import datetime


# print(dir(datetime))
# print(dir(datetime.MINYEAR))
# print(list(_ for _ in dir(datetime) if 'date' in _.lower()))
#
# print(help(datetime))  # documentation
# print(help(datetime.date))  # documentation


##############################################
#  Isolating project dependencies with Virtualenv
##############################################
# sudo apt install python3.9-venv
# paython3.9 -m venv venv

##############################################
#  Peeking behind the Bytecode curtain
##############################################
def greet(name):
    return f'Hello {str.capitalize(name)} !!'


print(greet('prashant'))
print(greet.__code__.co_code)
print(greet.__code__.co_consts)
print(greet.__code__.co_varnames)

import dis

print(dis.dis(greet))
