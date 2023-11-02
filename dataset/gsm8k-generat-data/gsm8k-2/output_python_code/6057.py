def solution():
    """Troy bakes 2 pans of brownies, cut into 16 pieces per pan. The guests eat all of 1 pan, and 75% of the 2nd pan. One tub of ice cream provides 8 scoops. If all but 4 of the guests eat the brownies ala mode (with 2 scoops of vanilla ice cream), how many tubs of ice cream did the guests eat?"""
    pan_size = 16
    total_brownies = 2 * pan_size
    eaten_brownies = pan_size + (0.75 * pan_size)
    guests = total_brownies - eaten_brownies
    ice_cream_scoops_per_guest = 2
    ice_cream_scoops_per_tub = 8
    total_ice_cream_scoops = guests * ice_cream_scoops_per_guest
    total_ice_cream_tubs = total_ice_cream_scoops / ice_cream_scoops_per_tub
    result = total_ice_cream_tubs
    return result

print(solution())