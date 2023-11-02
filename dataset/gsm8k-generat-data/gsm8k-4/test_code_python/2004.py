def solution():
    """The average of marks scored in four tests by Jake was 75. If jake scored 80 marks in the first test and 10 more in the second test, and an equal number of marks in the third and fourth test, calculate the marks he scored in the third test."""
    # Define the total average and the scores for the first two tests
    total_average = 75
    test1_score = 80
    test2_score = 90  # 10 more than the first test

    # Calculate the sum of scores for all four tests
    sum_scores = total_average * 4

    # Calculate the sum of scores for the third and fourth test
    sum_3rd_and_4th = sum_scores - test1_score - test2_score

    # Divide the sum of scores for the third and fourth test by 2 to get the score for each test
    test3_score = sum_3rd_and_4th / 2

    result = test3_score
    return result

print(solution())