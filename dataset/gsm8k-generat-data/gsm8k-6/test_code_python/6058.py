def solution():
    # Calculate the total number of brownie pieces
    total_brownies = 2 * 16  

    # Calculate the number of brownie pieces eaten by the guests
    brownies_eaten = 16 + (0.75 * 16)  # guests eat all of 1 pan and 75% of the 2nd pan

    # Calculate the number of guests who ate the brownies ala mode
    guests_alamode = brownies_eaten // 2 - 4  # all but 4 guests eat the brownies ala mode

    # Calculate the number of ice cream scoops needed
    ice_cream_scoops = 2 * guests_alamode  

    # Calculate the number of tubs of ice cream needed
    tubs_of_ice_cream = ice_cream_scoops // 8 + 1  # one tub provides 8 scoops

    result = tubs_of_ice_cream
    return result

print(solution())