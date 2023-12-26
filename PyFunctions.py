def fun1(x: int):
    """Return X*X number"""
    return x * x


def fun2(x: int):
    """Return X*X*X number"""
    return x * x * x


class SomeClass(object):
    pass


var = fun1
print(var(10))

var = fun2
print(var(20))

dict1 = {"fun1": lambda x: x * x, "fun2": lambda y: y * y * y}
print(dict1["fun1"](10))
print(dict1["fun2"](20))

# Class members

obj = SomeClass()
obj.newFun = fun1
print(obj.newFun(10))

obj.newFun = fun2
print(obj.newFun(20))
