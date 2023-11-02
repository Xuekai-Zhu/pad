def solution():
    # Calculate the total distance jumped by each athlete
    athlete1_total_distance = 26 + 30 + 7
    athlete2_total_distance = 24 + 34 + 8

    # Calculate the average distance jumped by each athlete
    athlete1_average_distance = athlete1_total_distance / 3
    athlete2_average_distance = athlete2_total_distance / 3

    # Determine the winner based on the highest average jump
    if athlete1_average_distance > athlete2_average_distance:
        winner_average_jump = athlete1_average_distance
    else:
        winner_average_jump = athlete2_average_distance
    
    result = winner_average_jump
    return result

print(solution())