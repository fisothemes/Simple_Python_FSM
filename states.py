################### CREATE YOUR STATE FUNCTIONS HERE ###########################

import globals                   # Importing global variable

def _init():
    # INIT STATE (initialization State)
    # Your initialization code goes here
    # Make sure you return the FIRST STATE after your init code
    print('\n Initializing')
    first_state = 'state_one'
    return first_state

def state_one():
    # FIRST STATE
    # Input the code for your state
    # Make sure you return the NEXT STATE when done executing
    print('\n Hello World!')
    next_state = 'state_two'
    return next_state

def state_two():
    # SECOND STATE
    # Input the code for your state
    # You can use global variables to pass data between states
    # Make sure you return the NEXT STATE when done executing

    print('\n What is your name?')
    globals.name = input(' Put name here: ')
    next_state = 'state_three'
    return next_state

def state_three():
    # THIRD STATE
    # Input the code for your state
    # You can use global variables to pass data between states
    # Return EXIT STATE when you are done with operation

    print('\n Nice to meet you', globals.name)
    exit_state = 'exit'
    return exit_state

def _exit():
    # EXIT STATE
    # Your clean up/code code goes here
    # Return not needed
    print('\n Goodbye World!')
    exit()
