def solution():
    easy_points = 6 * 2  # Kim got 6 correct answers in the easy round, worth 2 points each
    average_points = 2 * 3  # Kim got 2 correct answers in the average round, worth 3 points each
    difficult_points = 4 * 5  # Kim got 4 correct answers in the difficult round, worth 5 points each

    # Calculate the total points Kim scored in the contest
    total_points = easy_points + average_points + difficult_points
    result = total_points
    return result

print(solution())