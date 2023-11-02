def solution():
    """Maria's test scores are 80, 70, and 90. What score does she need to get on a fourth test so that her average score for the four tests is exactly 85?"""
    # Define the current test scores and the desired average
    test_scores = [80, 70, 90]
    desired_average = 85

    # Calculate the current average
    current_average = sum(test_scores) / len(test_scores)

    # Calculate the score Maria needs on the fourth test
    needed_score = (desired_average * (len(test_scores) + 1)) - sum(test_scores)

    # return the result
    result = needed_score
    return result

print(solution())