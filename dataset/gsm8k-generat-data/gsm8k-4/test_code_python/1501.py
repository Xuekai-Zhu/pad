def solution():
    """A tractor trailer has a load of 50000 pounds.  10% of the weight gets unloaded at the first store, and 20% of the remaining load is removed at the second store.  How much weight, in pounds, is left on the truck after the two deliveries?"""
    # Define the initial weight of the load
    initial_weight = 50000

    # Calculate the weight unloaded at the first store
    first_unloaded = initial_weight * 0.1

    # Calculate the remaining weight after the first store
    remaining_weight = initial_weight - first_unloaded

    # Calculate the weight unloaded at the second store
    second_unloaded = remaining_weight * 0.2

    # Calculate the final weight on the truck
    final_weight = remaining_weight - second_unloaded

    result = final_weight
    return result

print(solution())