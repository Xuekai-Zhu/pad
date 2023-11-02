def solution():
    """Rebecca makes her own earrings out of buttons, magnets, and gemstones.  For every earring, she uses two magnets, half as many buttons as magnets, and three times as many gemstones as buttons.  If Rebecca wants to make 4 sets of earrings, how many gemstones will she need?"""
    # Define the number of magnets, buttons, and gemstones per earring
    MAGNETS_PER_EARRING = 2
    BUTTONS_PER_EARRING = 1
    GEMSTONES_PER_EARRING = 3

    # Define the number of earrings per set
    EARRINGS_PER_SET = 2

    # Calculate the total number of magnets needed
    magnets_needed = MAGNETS_PER_EARRING * EARRINGS_PER_SET * 4

    # Calculate the total number of buttons needed
    buttons_needed = BUTTONS_PER_EARRING * EARRINGS_PER_SET * 4 * 0.5

    # Calculate the total number of gemstones needed
    gemstones_needed = GEMSTONES_PER_EARRING * BUTTONS_PER_EARRING * EARRINGS_PER_SET * 4 * 0.5 * 3

    # Display the total number of gemstones needed
    result = gemstones_needed
    return result

print(solution())