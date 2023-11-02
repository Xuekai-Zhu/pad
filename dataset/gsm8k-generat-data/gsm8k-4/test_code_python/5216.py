def solution():
    """Jacob takes four tests in his physics class and earns 85, 79, 92 and 84. What must he earn on his fifth and final test to have an overall average of 85?"""
    # Define the scores from the first four tests
    test1 = 85
    test2 = 79
    test3 = 92
    test4 = 84

    # Define the desired average score
    desired_average = 85

    # Calculate the total score from the first four tests
    total_score = test1 + test2 + test3 + test4

    # Calculate the minimum score needed on the fifth test to achieve the desired average
    min_score = (desired_average * 5) - total_score

    result = min_score
    return result

print(solution())