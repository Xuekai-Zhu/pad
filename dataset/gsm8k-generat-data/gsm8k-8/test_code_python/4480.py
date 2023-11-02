def solution():
    # Calculate the amount of cleaner used in the first 15 minutes
    first_15_minutes = 2 * 15

    # Calculate the amount of cleaner used in the next 10 minutes
    next_10_minutes = 3 * 10

    # Calculate the amount of cleaner used in the final 5 minutes
    final_5_minutes = 4 * 5

    # Calculate the total amount of cleaner used
    total_cleaner_used = first_15_minutes + next_10_minutes + final_5_minutes
    result = total_cleaner_used
    return result

print(solution())