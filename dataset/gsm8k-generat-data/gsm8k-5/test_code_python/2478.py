def solution():
    eric_points = 6  # Eric has 6 points
    mark_points = eric_points * 1.5 # Mark has 50% more points than Eric
    samanta_points = mark_points + 8 # Samanta has 8 more points than Mark

    # Calculate the total points for all three players
    total_points = eric_points + mark_points + samanta_points
    result = total_points
    return result

print(solution())