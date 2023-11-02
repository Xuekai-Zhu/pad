def solution():
    
    starting_buttons = 14
    shane_buttons = starting_buttons * 3
    remaining_buttons = starting_buttons + shane_buttons
    sam_buttons = remaining_buttons / 2
    mark_buttons = remaining_buttons - sam_buttons
    result = mark_buttons
    return result

print(solution())