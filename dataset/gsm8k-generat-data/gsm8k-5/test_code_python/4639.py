def solution():
    # Calculate points per minute
    points_per_minute = (2 * 2 + 1 * 3) / 4

    # Calculate total time played in minutes
    total_time = 2 * 12  # 2 periods, each 12 minutes long

    # Calculate total points scored
    total_points = points_per_minute * total_time
    result = total_points
    return result

print(solution())