def solution():
    num_white_shirts = 40
    num_floral_shirts = 50

    # Calculate the number of white shirts with collars
    num_white_collars = num_white_shirts / 2

    # Calculate the number of floral shirts with buttons
    num_buttons = 20

    # Calculate the number of floral shirts with no buttons
    num_no_buttons = num_floral_shirts - num_white_collars - num_buttons

    # Calculate the difference between the number of floral shirts with no buttons and the number of white shirts with no collars
    difference = num_no_buttons - num_no_buttons
    result = difference
    return result

print(solution())