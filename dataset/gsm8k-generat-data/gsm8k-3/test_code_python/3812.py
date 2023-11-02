def solution():
    """Don throws 3 darts.  One is a bullseye worth 50 points.  One completely missed the target, so received no points. The third was worth half the points of the bullseye.  What is the final score from these 3 throws?"""
    # Define the point values for each dart
    BULLSEYE_POINTS = 50
    HALF_BULLSEYE_POINTS = BULLSEYE_POINTS / 2
    MISSED_POINTS = 0

    # Calculate Don's final score
    score = BULLSEYE_POINTS + HALF_BULLSEYE_POINTS + MISSED_POINTS

    # Display Don's final score
    result = score
    return result

print(solution())