def solution():
    """A supplier is packing cartons of canned juice. Each carton has 20 cans of juice. Out of the 50 cartons that have been packed, only 40 cartons have been loaded on a truck. How many cans of juice are left to be loaded on the truck?"""
    cans_per_carton = 20
    total_cartons = 50
    loaded_cartons = 40
    remaining_cartons = total_cartons - loaded_cartons
    remaining_cans = remaining_cartons * cans_per_carton
    result = remaining_cans
    return result

print(solution())