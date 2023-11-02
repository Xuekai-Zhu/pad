def solution():
    """Carl is taking a class where the whole grade is based on four tests that are graded out of 100. He got an 80, a 75 and a 90 on his first three tests. If he wants an 85 average for the class, what is the minimum grade he needs to get on his last test?"""
    # Define the target average grade and the scores for the first three tests
    target_average = 85
    test_scores = [80, 75, 90]

    # Calculate the current average grade
    current_average = sum(test_scores) / len(test_scores)

    # Calculate the minimum score Carl needs on his last test to achieve the target average
    min_score = (target_average * 4) - sum(test_scores)

    # Return the result
    result = min_score
    return result

print(solution())