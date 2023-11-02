def solution():
    """A tractor trailer has a load of 50000 pounds.  10% of the weight gets unloaded at the first store, and 20% of the remaining load is removed at the second store.  How much weight, in pounds, is left on the truck after the two deliveries?"""
    # Define the initial load and the percentages of weight to be removed at each store
    initial_load = 50000
    removal_percentage_1 = 0.1
    removal_percentage_2 = 0.2

    # Calculate the weight removed at the first store
    weight_removed_1 = initial_load * removal_percentage_1

    # Calculate the remaining load
    remaining_load = initial_load - weight_removed_1

    # Calculate the weight removed at the second store
    weight_removed_2 = remaining_load * removal_percentage_2

    # Calculate the final load left on the truck
    final_load = remaining_load - weight_removed_2

    # Display the final load left on the truck
    result = final_load
    return result

print(solution())