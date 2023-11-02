def solution():
    """Lionel walked 4 miles. Esther walked 975 yards and Niklaus walked 1287 feet. How many combined feet did the friends walk?"""
    # Convert miles to feet
    lionel_feet = 4 * 5280

    # Convert yards to feet
    esther_feet = 975

    # Add feet walked
    niklaus_feet = 1287

    # Calculate the total feet walked
    total_feet = lionel_feet + esther_feet + niklaus_feet

    # Display the total feet walked
    result = total_feet
    return result

print(solution())