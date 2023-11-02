def solution():
    """If 8 carpenters can make 50 chairs in 10 days, how many carpenters are needed to make 75 chairs in 10 days?"""
    # Define the number of carpenters, chairs, and days for the initial scenario
    carpenters_initial = 8
    chairs_initial = 50
    days_initial = 10

    # Define the number of chairs for the desired scenario
    chairs_desired = 75

    # Calculate the number of carpenters needed for the desired scenario
    carpenters_desired = (carpenters_initial * chairs_desired * days_initial) / (chairs_initial * 10)

    # Round up to the nearest integer
    carpenters_desired = int(carpenters_desired + 0.5)

    # Return the result
    result = carpenters_desired
    return result

print(solution())