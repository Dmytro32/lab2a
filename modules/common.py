import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def Myfunction():
    i = 0
    A=input("True or False:")
    if not A=="True" and not A=="False":
        print ("Wrong text")
    else :
        for i in range(1,101):
            if  A=="True" and not   i%2==0:
                continue
            print(i)
def fun_with_error():
    return 5/0
