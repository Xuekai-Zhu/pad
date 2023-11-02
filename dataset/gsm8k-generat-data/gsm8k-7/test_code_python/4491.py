def solution():
    num_kids = 3
    shirts_per_kid = 3
    buttons_per_shirt = 7

    # Calculate the total number of shirts Jack sews
    total_shirts = num_kids * shirts_per_kid

    # Calculate the total number of buttons needed for all shirts
    total_buttons = total_shirts * buttons_per_shirt
    result = total_buttons
    return result

print(solution())