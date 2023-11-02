def solution():
    """Lionel walked 4 miles. Esther walked 975 yards and Niklaus walked 1287 feet. How many combined feet did the friends walk?"""
    # Define the conversion factors
    MILES_TO_FEET = 5280
    YARDS_TO_FEET = 3

    # Convert Lionel's distance to feet
    lionel_feet = 4 * MILES_TO_FEET

    # Convert Esther's distance to feet
    esther_feet = 975 * YARDS_TO_FEET

    # Convert Niklaus's distance to feet
    niklaus_feet = 1287

    # Calculate the total distance walked in feet
    total_feet = lionel_feet + esther_feet + niklaus_feet

    # return the result
    result = total_feet
    return result

print(solution())