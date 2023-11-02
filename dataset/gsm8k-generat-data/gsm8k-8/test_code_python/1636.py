def solution():
    # Calculate the total time Keegan spends in school each day in minutes
    total_time = 7.5 * 60

    # Subtract the time he spends in history and chemistry from the total time
    remaining_time = total_time - 90

    # Divide the remaining time by the number of classes to get the average time per class
    avg_time_per_class = remaining_time / 5

    # Convert the average time per class to minutes
    avg_time_in_minutes = avg_time_per_class / 60

    result = avg_time_in_minutes
    return result

print(solution())