def solution():
    """The ratio of fuel used in gallons to the distance covered in miles by Haley's car is 4:7. If Haley's car used 44 gallons of gas, calculate the distance it covered in miles."""
    # Define the ratio of fuel used to distance covered
    fuel_to_distance_ratio = 4/7

    # Calculate the distance covered using the given ratio and amount of fuel used
    distance_covered = fuel_to_distance_ratio * 44

    # Round the result to the nearest whole number
    result = round(distance_covered)

    return result

print(solution())