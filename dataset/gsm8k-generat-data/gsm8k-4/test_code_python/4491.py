def solution():
    """Jack sews 3 shirts for each of his 3 kids. He sews 7 buttons in each shirt. How many buttons must Jack use for all the shirts?"""
    # Define the number of kids and shirts per kid
    kids = 3
    shirts_per_kid = 3

    # Calculate the total number of shirts
    total_shirts = kids * shirts_per_kid

    # Calculate the total number of buttons
    total_buttons = total_shirts * 7

    result = total_buttons
    return result

print(solution())