def solution():
    normal_average = 2
    remaining_days = 100
    current_total = 430

    # Calculate the total amount of rain needed to reach the normal average for the remaining days
    remaining_amount = remaining_days * normal_average - current_total
    # Calculate the average amount of rain needed per day for the remaining days
    average_needed = remaining_amount / remaining_days
    result = average_needed
    return result

print(solution())