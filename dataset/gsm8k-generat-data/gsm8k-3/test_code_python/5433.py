def solution():
    """The ratio of fuel used in gallons to the distance covered in miles by Haley's car is 4:7. If Haley's car used 44 gallons of gas, calculate the distance it covered in miles."""
    # Define the ratio of fuel used to distance covered
    fuel_distance_ratio = 4/7

    # Define the amount of fuel used in gallons
    fuel_used = 44

    # Calculate the distance covered in miles
    distance_covered = fuel_distance_ratio * fuel_used

    # Display the distance covered
    result = distance_covered
    return result

print(solution())