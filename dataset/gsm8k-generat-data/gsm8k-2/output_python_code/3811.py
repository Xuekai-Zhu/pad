def solution():
    """Don throws 3 darts. One is a bullseye worth 50 points. One completely missed the target, so received no points. The third was worth half the points of the bullseye. What is the final score from these 3 throws?"""
    bullseye_points = 50
    half_bullseye_points = bullseye_points / 2
    total_points = bullseye_points + half_bullseye_points
    result = total_points
    return result

print(solution())