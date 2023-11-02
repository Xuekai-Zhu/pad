def solution():
    """Carl is taking a class where the whole grade is based on four tests that are graded out of 100. 
    He got an 80, a 75 and a 90 on his first three tests. If he wants an 85 average for the class, 
    what is the minimum grade he needs to get on his last test?"""
    # Define the desired average
    desired_average = 85

    # Define the scores on the first three tests
    test1_score = 80
    test2_score = 75
    test3_score = 90

    # Calculate the total score after the first three tests
    total_score = test1_score + test2_score + test3_score

    # Calculate the minimum score Carl needs on the last test to achieve the desired average
    min_test4_score = (desired_average * 4) - total_score

    # Display the minimum score Carl needs on the last test
    result = min_test4_score
    return result

print(solution())