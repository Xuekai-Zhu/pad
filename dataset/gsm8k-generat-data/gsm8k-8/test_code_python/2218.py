def solution():
    # Define the number of segments in each type of rattlesnake's tail
    eastern_tail_segments = 6
    western_tail_segments = 8

    # Calculate the percentage difference in tail size
    percent_difference = abs(eastern_tail_segments - western_tail_segments) / western_tail_segments * 100
    result = percent_difference
    return result

print(solution())