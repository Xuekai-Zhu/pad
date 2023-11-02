def solution():
    """Mark started the day with 14 buttons. His friend Shane gave him 3 times that amount of buttons. Then his other friend Sam asked if he could have half of Mark’s buttons. How many buttons did Mark end up with?"""
    # Define the number of buttons Mark started with
    starting_buttons = 14

    # Calculate the number of buttons Shane gave Mark
    shane_buttons = starting_buttons * 3

    # Calculate the number of buttons Sam took from Mark
    sam_buttons = starting_buttons / 2

    # Calculate the final number of buttons Mark has
    final_buttons = starting_buttons + shane_buttons - sam_buttons

    # Display the final number of buttons
    result = final_buttons
    return result

print(solution())