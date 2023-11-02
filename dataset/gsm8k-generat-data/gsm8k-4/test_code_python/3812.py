def solution():
    """Don throws 3 darts. One is a bullseye worth 50 points. One completely missed the target, so received no points. The third was worth half the points of the bullseye. What is the final score from these 3 throws?"""
    # Define the points earned for each throw
    bullseye_points = 50
    missed_points = 0
    third_points = bullseye_points / 2

    # Calculate the total score
    total_score = bullseye_points + missed_points + third_points

    # return the result
    result = total_score
    return result

print(solution())