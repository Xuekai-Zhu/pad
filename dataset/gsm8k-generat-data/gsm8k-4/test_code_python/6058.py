def solution():
    """Troy bakes 2 pans of brownies, cut into 16 pieces per pan.  The guests eat all of 1 pan, and 75% of the 2nd pan.  One tub of ice cream provides 8 scoops.  If all but 4 of the guests eat the brownies ala mode (with 2 scoops of vanilla ice cream), how many tubs of ice cream did the guests eat?"""
    # Define the number of brownie pans and the number of pieces per pan
    brownie_pans = 2
    pieces_per_pan = 16

    # Calculate the total number of brownie pieces
    total_pieces = brownie_pans * pieces_per_pan

    # Calculate the number of brownie pieces eaten by the guests
    pieces_eaten = (1 * pieces_per_pan) + (0.75 * pieces_per_pan)

    # Calculate the number of guests who ate brownies ala mode
    guests_ala_mode = total_pieces - 4

    # Calculate the total number of ice cream scoops needed
    ice_cream_scoops = guests_ala_mode * 2

    # Calculate the total number of ice cream tubs needed
    ice_cream_tubs = ice_cream_scoops / 8

    result = ice_cream_tubs
    return result

print(solution())