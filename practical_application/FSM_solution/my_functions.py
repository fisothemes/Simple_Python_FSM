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

def largerThanInput(data):
    dataAdder = []
    largestData = []
    print('PLEASE INPUT A VALUE TO FIND HOW MANY ARE LARGER THAN IT')
    while True:
        try:
            inputValue = float(input('Input Value Here: '))
            for i in x:
                if i > inputValue:
                    largestData.append(i)
                    dataAdder.append(i**0)
            largeMin = sum(dataAdder)
            print("\n"'These are the values of data greater than', inputValue)
            print('')
            print(largestData)
            print('')
            print(int(largeMin), 'out of',len(data) ,'experiments are larger than input value of', inputValue)
            break
        except ValueError:
            print('Sorry That wasnt a number')
