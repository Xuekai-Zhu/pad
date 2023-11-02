def solution():
    """Kendra made 4 more than five times as many decorated buttons as Mari. Sue made half as many as Kendra. Mari made 8 buttons. How many did Sue make?"""
    # Define the number of buttons Mari made
    mari_buttons = 8

    # Calculate the number of buttons Kendra made
    kendra_buttons = 5 * mari_buttons + 4

    # Calculate the number of buttons Sue made
    sue_buttons = kendra_buttons / 2

    # Display the number of buttons Sue made
    result = sue_buttons
    return result

print(solution())