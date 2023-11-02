def solution():
    laps_run = 24  # The winner runs 24 laps around the school
    lap_distance = 100  # One lap around the school is 100 meters
    total_distance = laps_run * lap_distance  # The total distance run by the winner
    time_in_minutes = 12  # The race lasts for 12 minutes

    # Calculate the total amount earned by the winner
    earnings = (total_distance / 100) * 3.5

    # Calculate the average earnings per minute
    earnings_per_minute = earnings / time_in_minutes
    result = earnings_per_minute
    return result

print(solution())