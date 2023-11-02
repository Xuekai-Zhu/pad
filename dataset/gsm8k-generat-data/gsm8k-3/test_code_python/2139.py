def solution():
    """If there are sixty-five dolphins in the ocean, and three times that number joins in from a river which has its mouth at the ocean, calculate the total number of dolphins in the ocean."""
    # Define the number of dolphins in the ocean
    dolphins_ocean = 65

    # Define the number of dolphins from the river
    dolphins_river = 3 * dolphins_ocean

    # Calculate the total number of dolphins
    total_dolphins = dolphins_ocean + dolphins_river

    # Display the total number of dolphins
    result = total_dolphins
    return result

print(solution())