def solution():
    starting_buttons = 14
    shane_buttons = starting_buttons * 3
    sam_buttons = starting_buttons / 2

    # Calculate total number of buttons Mark ends up with
    total_buttons = starting_buttons + shane_buttons - sam_buttons
    result = total_buttons
    return result

print(solution())