def solution():
    """Troy bakes 2 pans of brownies, cut into 16 pieces per pan. The guests eat all of 1 pan, and 75% of the 2nd pan. One tub of ice cream provides 8 scoops. If all but 4 of the guests eat the brownies ala mode (with 2 scoops of vanilla ice cream), how many tubs of ice cream did the guests eat?"""
    brownies_per_pan = 16
    pans_of_brownies = 2
    total_brownies = brownies_per_pan * pans_of_brownies
    guests_eat_first_pan = brownies_per_pan
    guests_eat_second_pan = int(0.75 * brownies_per_pan)
    total_guests = guests_eat_first_pan + guests_eat_second_pan - 4
    scoops_per_tub = 8
    scoops_per_brownie = 2
    total_scoops = total_guests * scoops_per_brownie
    total_tubs = total_scoops / scoops_per_tub
    result = total_tubs
    
    return result

print(solution())