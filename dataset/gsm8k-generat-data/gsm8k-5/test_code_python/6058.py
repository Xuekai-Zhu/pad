def solution():
    # Calculate the total number of brownie pieces
    total_brownie_pieces = 2 * 16  # Two pans of brownies, 16 pieces per pan

    # Calculate the number of brownie pieces eaten by the guests
    eaten_brownie_pieces = 16 + 0.75 * 16  # All of one pan, 75% of the other pan

    # Calculate the number of guests who eat the brownies ala mode
    guests_ala_mode = total_brownie_pieces - 4  # All guests except 4 eat the brownies ala mode

    # Calculate the total number of scoops of ice cream needed for the guests
    ice_cream_scoops = guests_ala_mode * 2  # 2 scoops of ice cream per guest

    # Calculate the total number of tubs of ice cream needed
    ice_cream_tubs = ice_cream_scoops / 8  # 8 scoops of ice cream per tub

    result = ice_cream_tubs
    return result

print(solution())