def solution():
    """In a town, there is a multi-story parking lot, which has room for 425 cars. The parking lot has 5 levels, each of the same size. How many more cars can one level fit if there are already 23 parked cars on that level?"""
    # Define the total number of parking spots and the number of levels
    total_spots = 425
    num_levels = 5

    # Calculate the total number of spots per level
    spots_per_level = total_spots / num_levels

    # Calculate the number of parked cars on all levels except the current one
    parked_cars = total_spots - spots_per_level

    # Calculate the number of available spots on the current level
    available_spots = spots_per_level - 23

    # Return the number of remaining available spots
    result = available_spots
    return result

print(solution())