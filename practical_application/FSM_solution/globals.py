#################### PUT YOUR GLOBAL VARIABLES HERE ############################

my_data=[]

file = open('results.txt', 'r')
for data in file: my_data.append([float(x) for x in data.split()])

_experiment = my_data[0]
_date = my_data[1]
_time = my_data[2]
_data = my_data[3]

################################ WARNING! ######################################
#           Beware of race conditions when using global variables!             #
#           Try to avoid using them as much as you can!                        #
################################################################################
