def solution():
    total_laps = 98
    saturday_laps = 27
    sunday_morning_laps = 15

    # Calculate the remaining laps that Jeff needs to complete
    remaining_laps = total_laps - saturday_laps - sunday_morning_laps
    result = remaining_laps
    return result

print(solution())