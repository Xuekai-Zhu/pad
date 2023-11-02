def solution():
    candy_bars_per_week = 2
    weeks_saved = 4
    total_weeks = 16

    # Calculate the total number of candy bars Kim received
    total_received = candy_bars_per_week * total_weeks

    # Calculate the total number of candy bars Kim ate
    total_eaten = total_weeks // weeks_saved

    # Calculate the total number of candy bars Kim saved
    total_saved = total_received - total_eaten
    result = total_saved
    return result

print(solution())