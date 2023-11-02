def solution():
    # Calculate Kim's total points in the contest
    easy_points = 2 * 6  # 6 correct answers in the easy round, 2 points for each
    average_points = 3 * 2  # 2 correct answers in the average round, 3 points for each
    difficult_points = 5 * 4  # 4 correct answers in the difficult round, 5 points for each
    total_points = easy_points + average_points + difficult_points
    result = total_points
    return result

print(solution())