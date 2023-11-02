def solution():
    # Define the number of magnets and calculate the number of buttons and gemstones needed for one earring
    magnets_per_earring = 2
    buttons_per_earring = magnets_per_earring / 2
    gemstones_per_earring = buttons_per_earring * 3

    # Calculate the total number of gemstones needed for four sets of earrings
    gemstones_total = gemstones_per_earring * 4 * 2
    # multiplied by 2 because every set has two earrings.

    result = gemstones_total
    return result

print(solution())