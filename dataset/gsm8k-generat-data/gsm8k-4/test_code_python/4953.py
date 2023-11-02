def solution():
    """A supplier is packing cartons of canned juice. Each carton has 20 cans of juice. Out of the 50 cartons that have been packed, only 40 cartons have been loaded on a truck. How many cans of juice are left to be loaded on the truck?"""
    # Define the number of cans per carton and the total number of cartons packed
    CANS_PER_CARTON = 20
    total_cartons = 50

    # Define the number of cartons loaded on the truck
    loaded_cartons = 40

    # Calculate the number of cans that have been loaded on the truck
    loaded_cans = loaded_cartons * CANS_PER_CARTON

    # Calculate the number of cans left to be loaded on the truck
    left_cans = (total_cartons - loaded_cartons) * CANS_PER_CARTON

    # return the result
    result = left_cans
    return result

print(solution())