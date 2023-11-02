def solution():
    """The average score on last week's Spanish test was 90.  Marco scored 10% less than the average test score and Margaret received 5 more points than Marco.  What score did Margaret receive on her test?"""
    # Define the average test score
    AVERAGE_SCORE = 90

    # Calculate Marco's score
    marco_score = AVERAGE_SCORE * 0.9

    # Calculate Margaret's score
    margaret_score = marco_score + 5

    # Display Margaret's score
    result = margaret_score
    return result

print(solution())