def solution():
    """Jack sews 3 shirts for each of his 3 kids. He sews 7 buttons in each shirt. How many buttons must Jack use for all the shirts?"""
    # Define the number of shirts and buttons per shirt
    NUM_SHIRTS_PER_KID = 3
    NUM_BUTTONS_PER_SHIRT = 7

    # Calculate the total number of shirts
    total_shirts = NUM_SHIRTS_PER_KID * 3

    # Calculate the total number of buttons
    total_buttons = total_shirts * NUM_BUTTONS_PER_SHIRT

    # Display the total number of buttons
    result = total_buttons
    return result

print(solution())