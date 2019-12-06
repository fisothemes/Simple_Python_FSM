################### CREATE YOUR STATE FUNCTIONS HERE ###########################

import globals

def _init():

    print('\n Initializing')
    first_state = 'state_one'
    return first_state

def state_one():

    print('\n Hello World!')
    next_state = 'state_two'
    return next_state

def state_two():

    print('\n What is your name?')
    globals.name = input(' Put name here: ')
    next_state = 'state_three'
    return next_state

def state_three():

    print('\n Nice to meet you', globals.name)
    exit_state = 'exit'
    return exit_state

def _exit():

    print('\n Goodbye World!')
    exit()
