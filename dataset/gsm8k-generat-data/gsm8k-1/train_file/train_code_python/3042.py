def solution():
    """Mark started the day with 14 buttons. His friend Shane gave him 3 times that amount of buttons. Then his other friend Sam asked if he could have half of Mark’s buttons. How many buttons did Mark end up with?"""
    starting_buttons = 14
    shane_buttons = starting_buttons * 3
    remaining_buttons = starting_buttons + shane_buttons
    sam_buttons = remaining_buttons / 2
    mark_buttons = remaining_buttons - sam_buttons
    result = mark_buttons
    return result

print(solution())