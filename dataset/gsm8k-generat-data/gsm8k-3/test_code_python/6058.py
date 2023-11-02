def solution():
    """Troy bakes 2 pans of brownies, cut into 16 pieces per pan.  The guests eat all of 1 pan, and 75% of the 2nd pan.  One tub of ice cream provides 8 scoops.  If all but 4 of the guests eat the brownies ala mode (with 2 scoops of vanilla ice cream), how many tubs of ice cream did the guests eat?"""
    # Define the number of pieces of brownies in one pan
    PIECES_PER_PAN = 16

    # Calculate the total number of pieces of brownies
    total_pieces = 2 * PIECES_PER_PAN

    # Calculate the number of pieces of brownies eaten by the guests
    pieces_eaten = PIECES_PER_PAN + 0.75 * PIECES_PER_PAN

    # Calculate the number of guests who ate the brownies ala mode
    guests_alamode = (total_pieces - pieces_eaten) * 2 - 4

    # Calculate the number of tubs of ice cream the guests ate
    tubs_ice_cream = guests_alamode // 8

    # Display the number of tubs of ice cream
    result = tubs_ice_cream
    return result

print(solution())