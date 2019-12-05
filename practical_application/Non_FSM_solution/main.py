###############################################################################################
##                                         MODULE 1                                          ##
###############################################################################################


from statistics import stdev
from statistics import pstdev
from statistics import mean
from math import sqrt
import os
from subprocess import call
import time as TIME

file = open('results.txt', 'r')
kujo_data=[]

for data in file:
    kujo_data.append([float(x) for x in data.split()])

number = kujo_data[0]
date = kujo_data[1]
time = kujo_data[2]
data = kujo_data[3]

###############################################################################################
##                                         MODULE 2                                          ##
###############################################################################################

#funtion2
print('')
#function2a
def maxminFinder(x):
    maximum = max(x)
    minimum = min(x)

    print('The maximum value is:', maximum)
    print('The minimum value is:', minimum)

#function2b
def statFinder(x):
    while True:
        try:
            print("\n"'The Sample Standard Deviation is:', stdev(x))
            print('The Population Standard Deviation is', pstdev(x))
            print('The average is:', mean(x))
            break
        except ValueError:
            print("\n"'The Starndard Deviation could not be found due to there being only 1 input value.')
            print("\n"'The average is:', mean(x))
            break

#funtion2c

def largerThanInput(x):
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
            print(int(largeMin), 'out of',len(x) ,'experiments are larger than input value of', inputValue)
            break
        except ValueError:
            print('Sorry That wasnt a number')
#funtion2d
def dataAscend(x):
    l = sorted(x)
    print('')
    print('Data in Ascending order: ', l)

def dataDescend(x):
    l = sorted(x, reverse = True)
    print('')
    print('Data in Descending order: ', l)


###############################################################################################
##                                         MODULE 3                                          ##
###############################################################################################

#Function3 for Experiment number
def expNoData():
    while True:
        try:
            minExpNo = int(input('Please input the lowest experiment number: '))
            maxExpNo = int(input('Please input the highest experiment number: '))
            x = minExpNo - 1
            y = maxExpNo
            dataExpNo = data[x:y]
            dateExpNo = date[x:y]
            timeExpNo = time[x:y]

            print("\n"'Dates for Experiment No. ranging between', minExpNo, 'and', maxExpNo, ':'"\n")
            print(dateExpNo)
            print("\n"'Times for Experiment No. ranging between', minExpNo, 'and', maxExpNo, ':'"\n")
            print(timeExpNo)
            print("\n"'This is the data for the experiment number ranging between', minExpNo, 'and', maxExpNo, ':'"\n")
            print(dataExpNo)
            dataAscend(dataExpNo)
            dataDescend(dataExpNo)
            maxminFinder(dataExpNo)
            statFinder(dataExpNo)
            largerThanInput(dataExpNo)
            break
        except ValueError:
            print("\n"'''SORRY.
The input was not found within the data list OR the inputs were in the wrong order
Please try again.'''"\n")

#Function3 for Date
def dateData():
    while True:
        try:
            dateInput = float(input('Input a date for your experiment (e.g 12.05): '))
            zero = 0
            locDate = []
            for i in date:
                if i == dateInput:
                    locDate.append(zero)
                zero = zero + 1
            x = min(locDate)
            y = max(locDate) + 1
            dateDataRange = data[x:y]
            dateTimeRange = time[x:y]
            dateExpNoRange = number[x:y]

            print("\n"'Experiment No. for date: ', dateExpNoRange)
            print("\n"'Times for date', dateInput, ':'"\n")
            print(dateTimeRange)
            print("\n"'This is the list for data of the date', dateInput)
            print('')
            print(dateDataRange)
            dataAscend(dateDataRange)
            dataDescend(dateDataRange)
            print('')
            maxminFinder(dateDataRange)
            statFinder(dateDataRange)
            print('')
            largerThanInput(dateDataRange)
            break
        except ValueError:
            print("\n"'Sorry the input date was not found. Please try again.'"\n")

#Function3 for Time
def timeData():
    while True:
        try:
            minTimeInput = float(input('Input the earliest time here: '))
            maxTimeInput = float(input('Input the latest time here: '))
            zero = 0
            timeTimeRange = []
            timeDataRange = []
            timeExpNo = []
            timeDateRange = []
            locTime = []
            for i in time:
                if i >= minTimeInput and i <= maxTimeInput:
                    locTime.append(zero)
                zero = zero + 1
            for i in locTime:
                timeTimeRange.append(time[i])
                locNo = i - 1
                if locNo >= 0:
                    timeDataRange.append(data[locNo])
                    timeExpNo.append(number[locNo])
                    timeDateRange.append(date[locNo])


            print("\n"'Experiment No. for time: ', timeExpNo)
            print("\n"'Experiment Dates: ', timeDateRange)
            print("\n"'This is the time between', minTimeInput,'and', maxTimeInput)
            print("\n",timeTimeRange)
            #print('This is the location: ',locTime)
            print("\n"'This is the data for the time ranging between', minTimeInput, 'and', maxTimeInput, ':')
            print(timeDataRange)
            dataAscend(timeDataRange)
            dataDescend(timeDataRange)
            print('')
            maxminFinder(timeDataRange)
            statFinder(timeDataRange)
            print('')
            #print(timeDataRange)
            largerThanInput(timeDataRange)
            break
        except ValueError:
            print("\n"'Im sorry the input value was not a number or data was not found. Please try again.'"\n")


###############################################################################################
##                                        MODULE 4                                           ##
###############################################################################################

def binarySearch(alist, x):
    l = sorted(alist)
    if len(l) == 0:
        return False
    else:
        midpoint = len(l)//2
        if l[midpoint]==x:
            return True
        else:
            if x<l[midpoint]:
                return binarySearch(l[:midpoint],x)
            else:
                return binarySearch(l[midpoint+1:],x)
def rounder(x):
    smallNo = []
    roundNum = []
    roundLoc = []
    zero = 0
    for i in data:
        if i < x:
            w = (i-x)*-1
            smallNo.append(w)
        if i > x:
            w = i - x
            smallNo.append(w)
    #print(smallNo)
    for i in data:
        v = i - x
        if v == min(smallNo) or v == -min(smallNo):
            roundNum.append(i)
    print('Rounded number/s are:',roundNum)
    for i in data:
        if i in roundNum:
            roundLoc.append(zero)
        zero = zero + 1
    #print('Location of rounded Numbers: ',roundLoc)
    for i in roundLoc:
        print("\n"'The value', x, 'was not found in the data list.'"\n"'The closest values are:')
        print(roundNum)
        print("\n"'The Experiment Number for the corisponding closest value to', x, 'in the rounded list is:', number[i])
        print('The date at which took place for experiment number', number[i], 'is:', date[i])
        print('The time at which took place for experiment number', number[i], 'is:', time[i])
        print('\n'*4)

def theFinder(x):
    zero = 0
    locData = []
    if binarySearch(data, x) == True:
        for i in data:
            if i == x:
                locData.append(zero)
            zero = zero + 1
    elif binarySearch(data, x) == False:
        rounder(x)
    #print(locData)
    for i in locData:
        print("\n"'The Experiment Number for', x, 'is:', number[i])
        print('The date at which', x, 'took place for experiment number', number[i], 'is:', date[i])
        print('The time at which', x, 'took place for experiment number', number[i], 'is:', time[i])
        print('\n'*4)



###############################################################################################
##                                         MAIN                                              ##
###############################################################################################
h = 6

def clear():
    os.system('CLS' if os.name == 'nt' else 'CLEAR')

while True:
    print("""
=====================================================
                       MAIN MENU
===================================================== """)

    print('\n''PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION')
    print('\n''1. Display Results for all data.')
    print('\n''2. Display Results for a portion of data')
    print('\n''3. Avanced Data Processing')
    print('\n''4. PANIC BUTTON!!!')
    print('\n''0. Exit''\n')
    print('\n'*h)
    n = input('INPUT NUMBER HERE: ')
    if n == '1':
        clear()
        while True:
            print('\n'*3)
            print("""
=====================================================
           DISPLAY RESULTS FOR ALL DATA
===================================================== """)

            print('\n''PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION')
            print('\n''1. Display the Maximum and Minimum for all Data.')
            print('\n''2. Display the Mean and Standard Deviation for all Data.')
            print('\n''3. Display Data.')
            print('\n''4. Display Data in Ascending and Descending order.')
            print('\n''5. Display Data for values larger than specific value.')
            print('\n''0. Exit or Main Menu''\n')
            print('\n'*h)
            n1 = input('INPUT NUMBER HERE: ')
            if n1 == '1':
                clear()
                print("""
=====================================================
           MAXIMUM AND MINIMUM
===================================================== """)

                maxminFinder(data)
                print('\n'*h)
            elif n1 == '2':
                clear()
                print("""
=====================================================
         AVERAGE AND STANDARD DEVIATION
===================================================== """)
                statFinder(data)
                print('\n'*h)
            elif n1 == '3':
                clear()
                print("""
=====================================================
                    ALL DATA
===================================================== """)

                print('\n'"These are the Experiment Numbers:"'\n')
                print(number)
                print('\n'"These are the Dates for the Experiment Data:"'\n')
                print(date)
                print('\n'"These are the Times for the Experiment Data:"'\n')
                print(time)
                print('\n'"This is the Experiment Data:"'\n')
                print(data)
                print('\n'*h)
            elif n1 == '4':
                clear()
                print("""
=====================================================
            ASCENDING AND DESENDING DATA
===================================================== """)

                dataAscend(data)
                dataDescend(data)
                print('\n'*h)
            elif n1 == '5':
                clear()
                print("""
=====================================================
           DATA LARGER THAN 'X'
===================================================== """)

                largerThanInput(data)
                print('\n'*26)
            elif n1 == '0':
                clear()
                break
            else:
                print("I'm sorry. The input is not recognised. Please try again.")
            Exit = input('Press any key to go back to menu or 0 to exit: ')
            if Exit == '0':
                clear()
                exit()

    elif n == '2':
        clear()
        while True:
            print('')
            print('''
=====================================================
     WHICH PORTION OF DATA WOULD YOU LIKE TO USE?
=====================================================''')
            print('\n'"PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION"'\n')
            print('1. Data within a range of Experiment Numbers')
            print('\n''2. Data from date')
            print('\n''3. Data within a time range')
            print('\n''0. Main Menu or Exit')
            print('\n'*h)


            n2 = input('INPUT A NUMBER HERE: ')
            clear()
            if n2 == '1':
                clear()
                print('')
                expNoData()
                print('')
            elif n2 == '2':
                clear()
                print('')
                dateData()
                print('')
            elif n2 == '3':
                clear()
                print('')
                timeData()
                print('')
            elif n2 == '0':
                clear()
                break
            else:
                print("I'm sorry. The input is not recognised. Please try again.")
            Exit = input('Press any key to go back to menu or 0 to exit: ')
            if Exit == '0':
                clear()
                exit()
    elif n== '3':
        clear()
        while True:
            print('\n'*3)
            print('''
=====================================================
              ADVANCED DATA PROCESSING
=====================================================''')
            print('\n'"PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION"'\n')
            print('1. Extract Experiment No., Date and Time from data value ')
            print('\n''2. Modify values in experiment')
            print('\n''3. Add values to experiment')
            print('\n''0. Main Menu or Exit')
            print('\n'*h)

            n3 = input('INPUT A NUMBER HERE: ')
            if n3 == '1':
                clear()
                while True:
                    try:
                        x = float(input('\n'"Input Data value: "))
                        break
                    except ValueError:
                        print("\n"'That is not a number. Try again'"\n")
                theFinder(x)
            elif n3 == '2':
                clear()
                print("\n"'WORK IN PROGRESS'"\n")
            elif n3 == '3':
                clear()
                print("\n"'WORK IN PROGRESS'"\n")
            elif n3 == '0':
                clear()
                break
            else:
                print("I'm sorry. The input is not recognised. Please try again.")
            Exit = input('Press any key to go back to menu or 0 to exit: ')
            if Exit == '0':
                clear()
                exit()
    elif n == '4':
        import webbrowser
        webbrowser.open_new('http://www.staggeringbeauty.com/')

    elif n == '0':
        exit()

    else:
        print("I'm sorry. The input is not recognised. Please try again.")
    Exit = input('Press any other key to go back to main menu or 0 to exit: ')
    if Exit == '0':
        exit()
