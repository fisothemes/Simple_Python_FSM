import os
import time
import globals
from statistics import stdev
from statistics import pstdev
from statistics import mean
from math import sqrt

def clear():
    os.system('CLS' if os.name == 'nt' else 'clear')

def sleep(seconds):
    time.sleep(seconds)

def dataAscend(data):
    l = sorted(data)
    return l

def dataDescend(data):
    l = sorted(data, reverse = True)
    return l

def maxminFinder(data, y):
    if y == 'max': return max(data)
    if y == 'min': return min(data)

def statFinder(data, y):
    if y == 'standard deviation': return stdev(data)
    if y == 'population standard deviation': return pstdev(data)
    if y == 'mean': return mean(data)

def largerThanInput(user_input, data):
    new_data = []
    for i in data:
        if i > user_input:
            new_data.append(i)
    return new_data
