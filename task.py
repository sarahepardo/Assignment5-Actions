import math


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

