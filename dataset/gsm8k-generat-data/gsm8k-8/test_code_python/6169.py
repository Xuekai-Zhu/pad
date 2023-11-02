def solution():
    # Define the distance to be covered for the marathon
    marathon_distance = 26.3

    # Define the initial distance Tomas can run
    initial_distance = 3

    # Calculate the number of months needed to double distance to marathon distance
    months_needed = math.ceil(math.log2(marathon_distance / initial_distance))

    # Calculate the total number of months needed for training
    total_months = months_needed + 1  # Add one to include the first month

    result = total_months
    return result

print(solution())