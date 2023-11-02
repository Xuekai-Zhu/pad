def solution():
    """The big bottles of mango juice hold 30 ounces and cost 2700 pesetas each. The small bottles hold 6 ounces and cost 600 pesetas each. How many pesetas would be saved by buying a big bottle instead of smaller bottles for the same volume of juice?"""
    big_bottle_cost = 2700
    small_bottle_cost = 600
    big_bottle_volume = 30
    small_bottle_volume = 6
    same_volume = big_bottle_volume / small_bottle_volume
    cost_of_same_volume_with_small = same_volume * small_bottle_cost
    saved_pesetas = cost_of_same_volume_with_small - big_bottle_cost
    result = saved_pesetas
    
    return result

print(solution())