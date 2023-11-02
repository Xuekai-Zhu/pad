def solution():
    old_average = 3  # Osborn's old average time to get dressed is 3 minutes
    current_total_time = 2 + 4 + 3 + 4  # Osborn's current total time for the week before Friday is 13 minutes
    remaining_days = 2  # Osborn has 2 days left to achieve his old average

    # Calculate the time required on Friday to tie his old average
    required_time_friday = (old_average * (remaining_days + 1)) - current_total_time
    required_speed_friday = required_time_friday / remaining_days
    result = required_speed_friday
    return result

print(solution())