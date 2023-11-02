def solution():
    # Define the total laps and laps swam on Saturday and Sunday morning
    total_laps = 98
    laps_saturday = 27
    laps_sunday_morning = 15

    # Calculate the remaining laps after Saturday and Sunday morning
    remaining_laps = total_laps - laps_saturday - laps_sunday_morning
    result = remaining_laps
    return result

print(solution())