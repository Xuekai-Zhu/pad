def solution():
    total_students = 45

    # Let x be the number of drunk drivers
    x = (total_students - 3) / 7

    # Round x up to the nearest whole number since it represents the number of people
    # and cannot be a fraction
    x = math.ceil(x)

    # Calculate the number of speeders
    num_speeders = 7*x - 3

    # Calculate the number of drunk drivers
    num_drunk_drivers = x

    result = num_drunk_drivers
    return result

print(solution())