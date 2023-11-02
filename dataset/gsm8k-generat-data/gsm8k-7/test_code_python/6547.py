def solution():
    num_shirts_monday = 4
    num_shirts_tuesday = 3
    num_shirts_wednesday = 2
    num_buttons_per_shirt = 5

    # Calculate the total number of shirts Sally sews
    total_num_shirts = num_shirts_monday + num_shirts_tuesday + num_shirts_wednesday

    # Calculate the total number of buttons Sally needs
    total_num_buttons = total_num_shirts * num_buttons_per_shirt
    result = total_num_buttons
    return result

print(solution())