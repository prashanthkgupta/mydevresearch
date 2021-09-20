# Underscore dubders and more
'''
Sengle Leading Underscore (_var) - Convention to tell programmers that this variable or function is for internal use,
                                    but if we import a module using wildcard import then _var wont get imported.

Trailing Leading Underscore (var_) - To avoid naming conflict with python keywords

Double Leading Underscore (__var) - python interpreter renames (name mangling) __var to _CLASS_NAME__var to avoid overriding from subclassed

Double Leading and Trailing Underscore (__var__) - name mangling is not done for these and used by python features

Single Underscore (_) - Sometimes used as name for temporary or insignificant variable.
                            also represents the result of last expression in a python REPL session
'''
_Test__bar3 = 17

class Test:
    def __init__(self):
        self._Test__bar2 = 10
        self.__bar2 = 1

    def printt(self):
        self._Test__bar2=7
        print(self._Test__bar2)
        print(__bar3)


Test().printt()  # prints 1 \n 1
print(dir(Test()))

