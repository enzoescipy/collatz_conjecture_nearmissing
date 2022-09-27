from glob import escape
from inspect import currentframe, getframeinfo
from pickle import TRUE


class debug:
    _DEBUG = False
    @classmethod
    def blocking(cls,*args):
        frameinfo = getframeinfo(currentframe().f_back)
        if cls._DEBUG == True:

            print(str(frameinfo.lineno) + " || " ,*args, end="")

            input("(press enter to go on) :")

    @classmethod
    def dprint(cls,*args, **kwargs):
        frameinfo = getframeinfo(currentframe().f_back)
        if cls._DEBUG == True:
            print(str(frameinfo.lineno) + " || ", end="")
            print(*args, **kwargs)
    

    @classmethod
    def on(cls):
        cls._DEBUG = True

    @classmethod
    def ison(cls):
        return cls._DEBUG