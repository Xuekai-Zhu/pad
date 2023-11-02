def solution():
    starting_buttons = 14  # Mark started with 14 buttons
    shane_buttons = 3 * starting_buttons  # Shane gave Mark 3 times as many buttons
    remaining_buttons = starting_buttons + shane_buttons  # Mark now has all the buttons
    sam_buttons = remaining_buttons / 2  # Sam takes half of the buttons

    # Calculate the final number of buttons Mark has
    final_buttons = remaining_buttons - sam_buttons
    result = final_buttons
    return result

print(solution())