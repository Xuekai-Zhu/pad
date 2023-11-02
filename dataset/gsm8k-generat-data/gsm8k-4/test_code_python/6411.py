def solution():
    """Rebecca makes her own earrings out of buttons, magnets, and gemstones. For every earring, she uses two magnets, half as many buttons as magnets, and three times as many gemstones as buttons. If Rebecca wants to make 4 sets of earrings, how many gemstones will she need?"""
    # Define the required materials for each earring
    magnets_per_earring = 2
    buttons_per_earring = magnets_per_earring / 2
    gemstones_per_earring = buttons_per_earring * 3

    # Calculate the total number of materials needed for 4 sets of earrings
    total_magnets = magnets_per_earring * 4 * 2  # 2 earrings per set, 4 sets
    total_buttons = buttons_per_earring * 4 * 2
    total_gemstones = gemstones_per_earring * 4 * 2

    # Return the total number of gemstones needed
    result = total_gemstones
    return result

print(solution())