def solution():
    """Sally sews 4 shirts on Monday, 3 shirts on Tuesday, and 2 shirts on Wednesday.  Each shirt has 5 buttons.  How many buttons does Sally need to sew all the shirts?"""
    # Define the number of shirts Sally sewed each day
    monday_shirts = 4
    tuesday_shirts = 3
    wednesday_shirts = 2

    # Define the number of buttons per shirt
    buttons_per_shirt = 5

    # Calculate the total number of buttons Sally needs
    total_buttons = (monday_shirts + tuesday_shirts + wednesday_shirts) * buttons_per_shirt

    # Display the total number of buttons Sally needs
    result = total_buttons
    return result

print(solution())