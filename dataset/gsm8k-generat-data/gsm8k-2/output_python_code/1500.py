def solution():
    """A tractor trailer has a load of 50000 pounds. 10% of the weight gets unloaded at the first store, and 20% of the remaining load is removed at the second store. How much weight, in pounds, is left on the truck after the two deliveries?"""
    load = 50000
    first_unload = 0.1 * load
    remaining_load = load - first_unload
    second_unload = 0.2 * remaining_load
    final_load = remaining_load - second_unload
    result = final_load
    return result

print(solution())