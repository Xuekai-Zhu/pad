def solution():
    
    # Define the number of buttons in the bag
    total_buttons = 21

    # Calculate the number of buttons with two holes
    buttons_with_two_holes = 7

    # Calculate the number of buttons with four holes
    buttons_with_four_holes = total_buttons - buttons_with_two_holes

    # Calculate the total number of holes in all the buttons
    total_holes = (buttons_with_two_holes * 2) + (buttons_with_four_holes * 4)

    # Display the total number of holes
    result = total_holes
    return result

print(solution())