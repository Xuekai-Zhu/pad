def solution():
    """A supplier is packing cartons of canned juice. Each carton has 20 cans of juice. Out of the 50 cartons that have been packed, only 40 cartons have been loaded on a truck. How many cans of juice are left to be loaded on the truck?"""
    # Define the number of cartons per pack and the number of cartons packed
    CARTONS_PER_PACK = 20
    packed_cartons = 50

    # Calculate the total number of cans in all the cartons
    total_cans = CARTONS_PER_PACK * packed_cartons

    # Calculate the number of cans in the cartons loaded on the truck
    loaded_cans = CARTONS_PER_PACK * 40

    # Calculate the number of cans left to be loaded on the truck
    cans_left = total_cans - loaded_cans

    # Display the number of cans left to be loaded
    result = cans_left
    return result

print(solution())