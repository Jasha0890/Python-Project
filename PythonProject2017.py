# function for assigning a user input float
def user_input_float():
    user_input = input("Please enter a float between 0 and 1: ")

    # while loop to continue loop until user has input a valid float value
    while type(user_input) != float:

        # try to float the user_input str
        try:
            user_input = float(user_input)

            # check if user_input float is between 0 and 1
            if user_input <= 0 or user_input >= 1:
                raise ValueError

        # catch exceptions to the above try, and reassign a value to user_input
        except ValueError:
            user_input = input("Incorrect input value. Please enter a float between 0 and 1: ")

    return user_input


# function for assigning a user input base
def user_input_base():
    user_input = input("Please enter a base between 2 and 16: ")

    # while loop to continue loop until user has input a valid base value
    while type(user_input) != int:

        # try to int the user_input str
        try:
            user_input = int(user_input)

            # check if user_input float is between 0 and 1
            if user_input < 0 or user_input > 16:
                raise ValueError

        # catch exceptions to the above try, and reassign a value to user_input
        except ValueError:
            user_input = input("Incorrect input value. Please enter a base between 2 and 16 again: ")

    return user_input


# function for returning converted number
def get_number(num):
    # use a dictionary to call numbers in str format by its key
    return {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F',
    }[num]


# function to return the number of decimal places in the original user input float number
def get_decimal_places(num):
    return len(str(num).split('.')[1])


# function to check if a float number is in a list
def check_infinite(number_list, number):
    if number in number_list:
        return True
    else:
        return False


# main function for converting the user input into a binary number
def converting():

    # assign the user_input_float to a variable
    float_for_op = user_input_float()

    # create original float variable to use in print later
    original_float = float_for_op

    # assign user_input_base to a variable
    original_base = user_input_base()

    # this is the variable to add all the binary numbers to get a final binary number
    final_number = '0.'

    # number of decimal places for rounding
    decimal_places = get_decimal_places(original_float)

    # initialise a previous numbers array to contain float_for_ops for comparison using check_infinite function
    previous_numbers = []

    # while loop to continue the converting algorithm
    while float_for_op != 0 and len(final_number) < 22:
        # multiply float_for_op by the base
        float_for_op *= original_base

        # Check to see if the new float_for_op is already in the previous numbers array
        if check_infinite(previous_numbers, float_for_op):
            print("WARNING: Periodic pattern detected!")
            break

        # append float_for_op into previous numbers array
        previous_numbers.append(float_for_op)

        # split the float_for_op and assign a variable name to each component (left side and right side of '.')
        integer, fraction = str(float_for_op).split('.')

        # turn the fraction into a float
        fraction = float('0.' + fraction)

        # round the fraction float
        # This part was necessary in order to produce accurate results as we experienced rounding errors with python.
        float_for_op = round(fraction, decimal_places)

        final_number += get_number(integer)

    print("{} in base 10 is {} in base {}.".format(original_float, final_number, original_base))
    print("Goodbye")

converting()
