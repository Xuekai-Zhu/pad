def solution():
    # Calculate the total time it takes to clean the apartment
    total_cleaning_time = (45 + 60 + 30 + (5 * 3))  # in minutes

    # Convert the free time from hours to minutes
    free_time = 3 * 60  # in minutes

    # Subtract the cleaning time from the free time to find the remaining free time
    remaining_free_time = free_time - total_cleaning_time
    result = remaining_free_time
    return result

print(solution())