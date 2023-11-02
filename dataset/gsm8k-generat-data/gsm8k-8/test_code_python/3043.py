def solution():
    # Define Mark's starting number of buttons
    mark_buttons = 14

    # Calculate how many buttons Shane gave Mark
    shane_buttons = 3 * mark_buttons

    # Calculate how many buttons Sam took from Mark
    sam_buttons = mark_buttons / 2

    # Calculate how many buttons Mark ended up with
    final_buttons = mark_buttons + shane_buttons - sam_buttons
    result = final_buttons
    return result

print(solution())