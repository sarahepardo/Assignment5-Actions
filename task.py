import math
from datetime import date


def firstrun():
    return "success"

def getarea(radius):
    area= math.pi * radius ** 2
    return area

def firstlastlist(List):
    size = len(List)
    first=List[0]
    last=List[size-1]
    return first & last

def differencedays(fyr,fmon,fday,lyr,lmon,lday):
    firstdate=date(fyr,fmon,fday)
    lastdate=date(lyr,lmon,lday)
    diff=lastdate-firstdate
    return diff


