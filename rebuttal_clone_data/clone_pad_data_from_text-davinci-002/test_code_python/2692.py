def solution():
    total_score = 90 + 98 + 92 + 94
    average_score = total_score / 4
    desired_average = 94
    points_needed = desired_average * 5 - total_score
    result = points_needed
    return result

print(solution())