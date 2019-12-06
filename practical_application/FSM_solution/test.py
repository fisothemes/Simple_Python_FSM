def main_menu():
            next_state = 'banana'
            user_input = input('INPUT OPTION HERE: ')
            print(user_input)
            if user_input == 1:
                next_state = 'compute_all_data'
                print(next_state)
            return next_state
    
x = main_menu()
print(x)
user_input = input('INPUT OPTION HERE: ')
print(user_input == '1')
