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
    print('These are the Dates for the Experiment Data: ')
    print('\n', globals._date)
    print('These are the Times for the Experiment Data: ')
    print('\n', globals._time)
    print('This is the Experiment Data: ')
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
    print('\n', dataAscend(globals._experiment))
    print('\n Descending: ')
    print('\n', dataDescend(globals._experiment))
    print('\n'*6)
