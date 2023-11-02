def solution():
    """The math questions in a contest are divided into three rounds: easy, average, and hard. There are corresponding points given for each round. That is 2, 3, and 5 points for every correct answer in the easy, average, and hard rounds, respectively. Suppose Kim got 6 correct answers in the easy; 2 correct answers in the average; and 4 correct answers in the difficult round, what are her total points in the contest?"""
    # Define the number of correct answers in each round
    easy_correct = 6
    average_correct = 2
    hard_correct = 4

    # Define the point value for each round
    easy_points = 2
    average_points = 3
    hard_points = 5

    # Calculate the total points earned
    total_points = (easy_correct * easy_points) + (average_correct * average_points) + (hard_correct * hard_points)

    # return the result
    result = total_points
    return result

print(solution())