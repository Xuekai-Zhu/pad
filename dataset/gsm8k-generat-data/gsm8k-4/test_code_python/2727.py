def solution():
    """Oshea bought 200 basil seeds. He wants to plant them in planters. He has 4 large planters that can hold 20 seeds each. He also has small planters that can hold 4 seeds each. How many small planters will he need to plant all the basil seeds?"""
    
    # Calculate the number of seeds that can be planted in the large planters
    large_planter_capacity = 4 * 20  

    # Calculate the number of seeds that can be planted in the small planters
    small_planter_capacity = 4 

    # Calculate the number of seeds that can be planted in both types of planters
    total_capacity = large_planter_capacity + small_planter_capacity 

    # Calculate the number of small planters needed to plant all the basil seeds
    small_planters_needed = (200 - large_planter_capacity) // small_planter_capacity 

    # If there are any remaining seeds, add one more small planter
    if (200 - large_planter_capacity) % small_planter_capacity != 0: 
        small_planters_needed += 1

    result = small_planters_needed
    return result

print(solution())