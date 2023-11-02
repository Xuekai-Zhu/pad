def solution():
    
    initial_buttons = 14
    shane_buttons = 3 * initial_buttons
    remaining_buttons = initial_buttons + shane_buttons
    sam_buttons = remaining_buttons / 2
    mark_buttons = remaining_buttons - sam_buttons
    result = mark_buttons
    return result

print(solution())