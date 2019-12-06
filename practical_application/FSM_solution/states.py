################### CREATE YOUR STATE FUNCTIONS HERE ###########################

import my_ui

def _init():
    my_ui._init()
    return 'main_menu'

def _error():
    my_ui._error()
    return 'main_menu'

def _exit():
    my_ui._exit
    exit()
    return '_exit'

def main_menu():
    my_ui.main_menu()
    try:
        next_state = int(input('INPUT OPTION HERE: '))
        if next_state == 0: return '_exit'
        if next_state == 1: return 'compute_all_data'
        if next_state == 2: return 'compute_partial_data'
        if next_state == 3: return 'advanced_data_processing'
    except:
        return 'main_menu'

############################ MAIN MENU STATES ##################################

def compute_all_data():
    my_ui.compute_all_data()
    try:
        next_state = int(input('INPUT OPTION HERE: '))
        if next_state == 0: return 'main_menu'
        if next_state == 1: return 'display_data'
        if next_state == 2: return 'display_ordered_data'
        if next_state == 3: return 'display_greater_than_data'
        if next_state == 4: return 'display_max_min_data'
        if next_state == 5: return 'display_mean_sd_data'
    except:
        return 'compute_all_data'

def compute_partial_data():
    my_ui.compute_partial_data()
    try:
        next_state = int(input('INPUT OPTION HERE: '))
        if next_state == 0: return 'main_menu'
        if next_state == 1: return 'display_exp_ranged_data'
        if next_state == 2: return 'display_date_ranged_data'
        if next_state == 3: return 'display_time_ranged_data'
    except:
        return 'compute_partial_data'

def advanced_data_processing():
    my_ui.advanced_data_processing()
    try:
        next_state = int(input('INPUT OPTION HERE: '))
        if next_state == 0: return 'main_menu'
        if next_state == 1:
            import webbrowser
            webbrowser.open_new('http://www.staggeringbeauty.com/')
            return '_error'
    except:
        return 'advanced_data_processing'

###################### COMPUTE ALL DATA STATES ################################

def display_data():
    my_ui.display_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_all_data'

def display_ordered_data():
    my_ui.display_ordered_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_all_data'

def display_greater_than_data():
    my_ui.display_greater_than_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_all_data'

def display_max_min_data():
    my_ui.display_max_min_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_all_data'

def display_mean_sd_data():
    my_ui.display_mean_sd_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_all_data'

###################### COMPUTE ALL DATA STATES ################################

def display_exp_ranged_data():
    my_ui.display_exp_ranged_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_partial_data'

def display_date_ranged_data():
    my_ui.display_date_ranged_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_partial_data'

def display_time_ranged_data():
    my_ui.display_time_ranged_data()
    previous_state = input('INPUT ANY VALUE TO RETURN: ')
    return 'compute_partial_data'
