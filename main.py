####################### RUN YOUR STATE MACHINE #################################
import states                           #Imports States

state = states.init()                   #INITIALIZING STATE
while True:

    if state == 'state_one':            #FIRST STATE
        state = states.state_one()

    if state == 'state_two':            #SECOND STATE
        state = states.state_two()

    if state == 'state_three':          #THIRD STATE
        state = states.state_three()

    if state == 'exit':                 #EXIT STATE
        state = states.exit()
        break
