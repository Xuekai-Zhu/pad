def solution():
    """The ratio of fuel used in gallons to the distance covered in miles by Haley's car is 4:7. If Haley's car used 44 gallons of gas, calculate the distance it covered in miles."""
    fuel_distance_ratio = 4 / 7
    fuel_used = 44
    distance_covered = fuel_used / fuel_distance_ratio
    result = distance_covered
    return result

print(solution())