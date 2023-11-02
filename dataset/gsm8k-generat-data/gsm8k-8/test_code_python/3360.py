def solution():
    # Define the number of original animal types and the time to see them
    original_types = 5
    original_time = 6 * original_types

    # Define the number of new animal types and the time to see them
    new_types = 4
    new_time = 6 * new_types

    # Calculate the total time to see all animal types
    total_time = original_time + new_time
    result = total_time
    return result

print(solution())