def solution():
    num_kids = 3  # Jack has 3 kids
    shirts_per_kid = 3  # Jack sews 3 shirts for each of his kids
    buttons_per_shirt = 7  # Jack sews 7 buttons on each shirt

    # Calculate the total number of shirts
    total_shirts = num_kids * shirts_per_kid

    # Calculate the total number of buttons
    total_buttons = total_shirts * buttons_per_shirt
    result = total_buttons
    return result

print(solution())