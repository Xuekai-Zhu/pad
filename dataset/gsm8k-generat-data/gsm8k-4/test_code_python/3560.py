def solution():
    """Anna wants to grow some lettuce in the garden and would like to grow enough to have at least 12 large salads. 
    She estimates that, despite her best efforts, half of the lettuce will be lost to insects and rabbits. 
    Each lettuce plant is estimated to provide 3 large salads. How many lettuce plants should Anna grow in the garden?"""
    # Define the number of large salads Anna wants
    large_salads = 12

    # Calculate the number of lettuce plants needed, taking into account half of them will be lost to insects and rabbits
    lettuce_plants_needed = large_salads * 2 / 3

    # Round up to the nearest whole number to ensure enough lettuce
    lettuce_plants_needed = round(lettuce_plants_needed + 0.5)

    # return the result
    result = lettuce_plants_needed
    return result

print(solution())