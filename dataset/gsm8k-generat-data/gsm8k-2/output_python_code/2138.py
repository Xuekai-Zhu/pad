def solution():
    """If there are sixty-five dolphins in the ocean, and three times that number joins in from a river which has its mouth at the ocean, calculate the total number of dolphins in the ocean."""
    ocean_dolphins = 65
    river_dolphins = 3 * ocean_dolphins
    total_dolphins = ocean_dolphins + river_dolphins
    result = total_dolphins
    return result

print(solution())