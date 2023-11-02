def solution():
    """A certain kind of wild mushroom has either spots or gills, but never both. Gilled mushrooms are rare, with only one growing for every nine spotted mushrooms that grow. A fallen log had 30 mushrooms growing on its side. How many gilled mushrooms were on the fallen log’s side?"""
    # Define the ratio of spotted to gilled mushrooms
    RATIO = 9

    # Calculate the number of spotted mushrooms
    spotted_count = 30 // (RATIO + 1)

    # Calculate the number of gilled mushrooms
    gilled_count = spotted_count // RATIO

    # Display the number of gilled mushrooms
    result = gilled_count
    return result

print(solution())