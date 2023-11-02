def solution():
    # Calculate the total number of brownie pieces Troy baked
    total_brownie_pieces = 2 * 16

    # Calculate the number of brownie pieces the guests ate
    guests_brownies = 16 + 0.75 * 16

    # Calculate the number of guests who ate brownies ala mode
    guests_ala_mode = total_brownie_pieces - guests_brownies - 4

    # Calculate the number of tubs of ice cream the guests ate
    tubs_ice_cream = guests_ala_mode * 2 / 8

    result = tubs_ice_cream
    return result

print(solution())