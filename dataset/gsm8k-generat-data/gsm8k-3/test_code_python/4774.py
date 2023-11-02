def solution():
    """Two athletes decided to compete to see who had the best jumping ability. They were each going to do the long jump, triple jump, and high jump to see who had the highest average jump. The first athlete jumped 26 feet in the long jump, 30 feet in the triple jump, and 7 feet in the high jump. The second athlete jumped 24 feet in the long jump, 34 feet in the triple jump, and 8 feet in the high jump. What was the average jump of the winner?"""
    # Calculate the total distance jumped by the first athlete
    athlete1_total_distance = 26 + 30 + 7

    # Calculate the total distance jumped by the second athlete
    athlete2_total_distance = 24 + 34 + 8

    # Calculate the average distance jumped by each athlete
    athlete1_avg_distance = athlete1_total_distance / 3
    athlete2_avg_distance = athlete2_total_distance / 3

    # Determine which athlete had the highest average jump
    if athlete1_avg_distance > athlete2_avg_distance:
        winner_avg_jump = athlete1_avg_distance
    else:
        winner_avg_jump = athlete2_avg_distance

    # Display the average jump of the winner
    result = winner_avg_jump
    return result

print(solution())