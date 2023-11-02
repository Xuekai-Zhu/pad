def solution():
    """Anna wants to grow some lettuce in the garden and would like to grow enough to have at least 12 large salads. She estimates that, despite her best efforts, half of the lettuce will be lost to insects and rabbits. Each lettuce plant is estimated to provide 3 large salads. How many lettuce plants should Anna grow in the garden?"""
    # Define the number of large salads Anna wants to have
    LARGE_SALADS = 12

    # Calculate the number of lettuce plants needed
    lettuce_plants = LARGE_SALADS * 2 / 3

    # Round up to the nearest whole number of lettuce plants needed
    lettuce_plants = math.ceil(lettuce_plants)

    # Display the number of lettuce plants needed
    result = lettuce_plants
    return result

print(solution())