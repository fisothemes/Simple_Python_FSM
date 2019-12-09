################################ UI ELEMENTS ##################################

#Clears previous UI
#UI height - 16 lines
#Makes UI for states

import globals
import my_functions

from my_functions import clear
from my_functions import sleep
from my_functions import dataAscend
from my_functions import dataDescend
from my_functions import maxminFinder
from my_functions import statFinder
from my_functions import largerThanInput



def _init():
    clear()
    print('''






=====================================================
                      INITIALIZING
=====================================================






    ''')

def _error():
    clear()
    print('''






=====================================================
                      ERROR!
=====================================================






    ''')
    sleep(1)

def _exit():
    clear()
    print('''






=====================================================
                      GOODBYE!
=====================================================






    ''')

def main_menu():
    clear()
    print('''
=====================================================
                    MAIN MENU
=====================================================

PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION
    1. Display Results for all data.
    2. Display Results for a portion of data.
    3. Advanced Data Processing.
    0. Exit







    ''')

############################# MAIN MENU UIs ###################################

def compute_all_data():
    clear()
    print('''
=====================================================
                COMPUTE ALL DATA
=====================================================

PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION
    1. Display Data.
    2. Display Data in Ascending and Descending order.
    3. Display Data for values larger than specified
       value.
    4. Display the Maximum and Minimum for all Data.
    5. Display the Mean and Standard Deviation for all
       Data.
    0. Main Menu



    ''')
def compute_partial_data():
    clear()
    print('''
=====================================================
                COMPUTE PARTIAL DATA
=====================================================

PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION
    1. Get data within a range of experiments.
    2. Get data within a range of a dates.
    3. Get data within a period of time.
    0. Main Menu







    ''')

def advanced_data_processing():
    clear()
    print('''
=====================================================
            ADVANCED DATA PROCESSING
=====================================================

PLEASE PRESS A NUMBER ON KEYBOARD TO SELECT AN OPTION
    1. UNDER CONSTRUCTION!
    0. Main Menu







    ''')

########################## COMPUTE ALL DATA UIs ################################

def display_data():
    clear()
    print('''
=====================================================
                    ALL DATA
=====================================================

    ''')
    print('These are the Experiment Numbers: ')
    print('\n', globals._experiment)
    print('\n These are the Dates for the Experiment Data: ')
    print('\n', globals._date)
    print('\n These are the Times for the Experiment Data: ')
    print('\n', globals._time)
    print('\n This is the Experiment Data: ')
    print('\n', globals._data)
    print('\n'*3)

def display_ordered_data():
    clear()
    print('''
=====================================================
            ORDERED EXPERIMENTAL DATA
=====================================================

    ''')
    print('Ascending: ')
    print('\n', dataAscend(globals._data))
    print('\n Descending: ')
    print('\n', dataDescend(globals._data))
    print('\n'*6)

def display_greater_than_data():
    clear()
    print('''
=====================================================
 DISPLAY EXPERIMENTAL DATA OF VALUES GREATER THAN...
=====================================================

    ''')
    try:
        user_input = float(input('\n Input Value Here: '))
        print('\n This is the Experimental data for values greater that ', user_input)
        print('\n',largerThanInput(user_input , globals._data))
    except:
        print('\n Thats not a number try again.')
    print('\n'*6)

def display_max_min_data():
    clear()
    print('''
=====================================================
                MAXIMUM & MINIMUM
=====================================================

    ''')

    print('\n This is the maximum experimental value:  ')
    print('\n',maxminFinder(globals._data, 'max'))
    print('\n This is the minimum experimental value:  ')
    print('\n',maxminFinder(globals._data, 'min'))

    print('\n'*4)

def display_mean_sd_data():
    clear()
    print('''
=====================================================
                MEAN & STANDARD DEVIATION
=====================================================

    ''')

    print('\n This is the mean of the experimental data:  ')
    print('\n',statFinder(globals._data, 'mean'))
    print('\n This is the standard deviation of experimental data:  ')
    print('\n',statFinder(globals._data, 'standard deviation'))
    print('\n This is the population standard deviation experimental data:  ')
    print('\n',statFinder(globals._data, 'population standard deviation'))
    print('\n'*2)

########################## COMPUTE PARTIAL DATA UIs ################################