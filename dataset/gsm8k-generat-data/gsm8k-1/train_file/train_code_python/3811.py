def solution():
    """Don throws 3 darts. One is a bullseye worth 50 points. One completely missed the target, so received no points. The third was worth half the points of the bullseye. What is the final score from these 3 throws?"""
    bullseye = 50
    missed = 0
    half_bullseye = bullseye/2
    total_score = bullseye + missed + half_bullseye
    result = total_score
    return result

print(solution())