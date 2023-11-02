def solution():
    """Mari made 4 more than five times as many decorated buttons as Kendra. Sue made half as many as Kendra. Sue made 6 buttons. How many did Mari make?"""
    # Define the number of buttons Sue made
    SUE_BUTTONS = 6

    # Calculate the number of buttons Kendra made
    kendra_buttons = SUE_BUTTONS * 2

    # Calculate the number of buttons Mari made
    mari_buttons = (5 * kendra_buttons) + 4

    # Display the number of buttons Mari made
    result = mari_buttons
    return result

print(solution())