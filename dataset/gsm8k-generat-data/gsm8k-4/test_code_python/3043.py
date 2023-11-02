def solution():
    """Mark started the day with 14 buttons. His friend Shane gave him 3 times that amount of buttons. Then his other friend Sam asked if he could have half of Mark’s buttons. How many buttons did Mark end up with?"""
    # Define the initial number of buttons
    initial_buttons = 14

    # Define the number of buttons Shane gave Mark
    shane_buttons = initial_buttons * 3

    # Define the number of buttons Mark had after receiving Shane's buttons
    total_buttons = initial_buttons + shane_buttons

    # Define the number of buttons Sam received
    sam_buttons = total_buttons / 2

    # Define the number of buttons Mark has left
    mark_buttons = total_buttons - sam_buttons

    # return the result
    result = mark_buttons
    return result

print(solution())