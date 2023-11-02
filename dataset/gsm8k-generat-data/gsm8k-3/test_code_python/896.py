def solution():
    """The math questions in a contest are divided into three rounds: easy, average, and hard. There are corresponding points given for each round. That is 2, 3, and 5 points for every correct answer in the easy, average, and hard rounds, respectively. Suppose Kim got 6 correct answers in the easy; 2 correct answers in the average; and 4 correct answers in the difficult round, what are her total points in the contest?"""
    # Define the points per correct answer
    EASY_POINTS = 2
    AVERAGE_POINTS = 3
    HARD_POINTS = 5

    # Get the number of correct answers in each round
    easy_correct = 6
    average_correct = 2
    hard_correct = 4

    # Calculate the total points
    total_points = easy_correct * EASY_POINTS + average_correct * AVERAGE_POINTS + hard_correct * HARD_POINTS

    # Display the total points
    result = total_points
    return result

print(solution())