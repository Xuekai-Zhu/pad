def solution():
    total_laps = 98  # Jeff has to swim a total of 98 laps
    saturday_laps = 27  # Jeff swam 27 laps on Saturday
    sunday_morning_laps = 15  # Jeff swam 15 laps on Sunday morning
    remaining_laps = total_laps - saturday_laps - sunday_morning_laps  # Jeff has to swim the remaining laps

    result = remaining_laps
    return result

print(solution())