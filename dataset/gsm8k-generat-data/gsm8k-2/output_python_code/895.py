def solution():
    """
    The math questions in a contest are divided into three rounds: easy, average, and hard.
    There are corresponding points given for each round. That is 2, 3, and 5 points for every correct answer
    in the easy, average, and hard rounds, respectively. Suppose Kim got 6 correct answers in the easy;
    2 correct answers in the average; and 4 correct answers in the difficult round,
    what are her total points in the contest?
    """
    easy_points = 6 * 2
    average_points = 2 * 3
    hard_points = 4 * 5
    total_points = easy_points + average_points + hard_points
    result = total_points
    return result

print(solution())