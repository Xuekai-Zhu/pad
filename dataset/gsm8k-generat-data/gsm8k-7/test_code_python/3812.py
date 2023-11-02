def solution():
    bullseye_points = 50
    missed_points = 0
    third_throw_points = bullseye_points / 2

    # Calculate the total score from all three throws
    total_score = bullseye_points + missed_points + third_throw_points
    result = total_score
    return result

print(solution())