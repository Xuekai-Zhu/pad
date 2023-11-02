def solution():
    fences_per_hour = 2  # Abigail builds 2 fences per hour
    hours_worked = 8  # Abigail works for 8 hours

    # Calculate the total number of fences Abigial builds in 8 hours
    total_fences = fences_per_hour * hours_worked

    # Calculate the total time Abigail spends building fences
    total_time = 10 * 0.5 + hours_worked

    result = total_fences + 10
    return result

print(solution())