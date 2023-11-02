def solution():
    # Calculate the total hours already completed
    total_hours_completed = 50 + 9 + 121

    # Calculate the remaining hours
    remaining_hours = 1500 - total_hours_completed

    # Calculate the number of months needed to complete the remaining hours
    months_needed = remaining_hours / 220

    result = months_needed
    return result

print(solution())