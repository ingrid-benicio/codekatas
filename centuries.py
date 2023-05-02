import math
from math import ceil

def centuries (year):
    #return year / 100 #that was my frist try but didnt meet the tests 
    #return round((year + 99) / 100)
    #return math.ceil(year/100)
    return -(-year // 100) #i got this from https://stackoverflow.com/questions/46356820/year-to-century-function 


print (centuries(1601))
    