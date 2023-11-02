def solution():
    # Calculate the total distance jumped by each athlete
    total_distance_athlete_1 = 26 + 30 + 7
    total_distance_athlete_2 = 24 + 34 + 8

    # Calculate the average distance of each athlete
    avg_distance_athlete_1 = total_distance_athlete_1 / 3
    avg_distance_athlete_2 = total_distance_athlete_2 / 3

    # Determine who has the highest average jump
    if avg_distance_athlete_1 > avg_distance_athlete_2:
        winner_avg_jump = avg_distance_athlete_1
    else:
        winner_avg_jump = avg_distance_athlete_2

    result = winner_avg_jump
    return result

print(solution())