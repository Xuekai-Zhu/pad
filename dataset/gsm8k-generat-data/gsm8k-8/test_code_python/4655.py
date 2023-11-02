def solution():
    # Calculate the total practice time in minutes
    total_practice_time = 7.5 * 60

    # Calculate the total practice time on the 2 days
    practice_time_on_2_days = 2 * 86

    # Calculate the remaining practice time
    remaining_practice_time = total_practice_time - practice_time_on_2_days

    # Convert the remaining practice time to minutes
    remaining_practice_time_minutes = int(remaining_practice_time % 60)

    result = remaining_practice_time_minutes
    return result

print(solution())