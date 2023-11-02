def solution():
    athlete1_long_jump = 26
    athlete1_triple_jump = 30
    athlete1_high_jump = 7

    athlete2_long_jump = 24
    athlete2_triple_jump = 34
    athlete2_high_jump = 8

    # Calculate the total distance jumped by each athlete
    athlete1_total_distance = athlete1_long_jump + athlete1_triple_jump + athlete1_high_jump
    athlete2_total_distance = athlete2_long_jump + athlete2_triple_jump + athlete2_high_jump

    # Calculate the average jump of each athlete
    athlete1_avg_jump = athlete1_total_distance / 3
    athlete2_avg_jump = athlete2_total_distance / 3

    # Determine the winner
    if athlete1_avg_jump > athlete2_avg_jump:
        winner_avg_jump = athlete1_avg_jump
    else:
        winner_avg_jump = athlete2_avg_jump

    result = winner_avg_jump
    return result

print(solution())