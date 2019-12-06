####################### RUN YOUR STATE MACHINE #################################
import states                               #Imports States

state = states._init()                      #INITIALIZING STATE
while True:
    if state == 'main_menu': state = states.main_menu()
    elif state == 'compute_all_data': state = states.compute_all_data()
    elif state == 'compute_partial_data': state = states.compute_partial_data()
    elif state == 'advanced_data_processing': state = states.advanced_data_processing()
    elif state == '_exit': state = states._exit()

    elif state == 'display_data': state = states.display_data()
    elif state == 'display_ordered_data': state = states.display_ordered_data()
    elif state == 'display_greater_than_data': state = states.display_greater_than_data()
    elif state == 'display_max_min_data': state = states.display_max_min_data()
    elif state == 'display_mean_sd_data': state = states.display_mean_sd_data()

    else: state = states._error()             #ERROR STATE
