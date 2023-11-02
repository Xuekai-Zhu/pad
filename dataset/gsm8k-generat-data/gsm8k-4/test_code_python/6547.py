def solution():
    """Sally sews 4 shirts on Monday, 3 shirts on Tuesday, and 2 shirts on Wednesday. Each shirt has 5 buttons. How many buttons does Sally need to sew all the shirts?"""
    # Define the number of shirts sewn each day
    shirts_monday = 4
    shirts_tuesday = 3
    shirts_wednesday = 2

    # Define the number of buttons per shirt
    buttons_per_shirt = 5

    # Calculate the total number of shirts
    total_shirts = shirts_monday + shirts_tuesday + shirts_wednesday

    # Calculate the total number of buttons needed
    total_buttons = total_shirts * buttons_per_shirt

    # Return the result
    result = total_buttons
    return result

print(solution())