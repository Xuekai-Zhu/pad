def solution():
    """A certain kind of wild mushroom has either spots or gills, but never both. Gilled mushrooms are rare, with only one growing for every nine spotted mushrooms that grow. A fallen log had 30 mushrooms growing on its side. How many gilled mushrooms were on the fallen log’s side?"""
    # Define the ratio of spotted to gilled mushrooms
    ratio_spotted = 9
    ratio_gilled = 1

    # Calculate the total number of mushrooms on the log's side
    total_mushrooms = 30

    # Calculate the number of spotted mushrooms
    spotted_mushrooms = total_mushrooms / (ratio_spotted + ratio_gilled) * ratio_spotted

    # Calculate the number of gilled mushrooms
    gilled_mushrooms = total_mushrooms - spotted_mushrooms

    # Return the number of gilled mushrooms
    result = gilled_mushrooms
    return result

print(solution())