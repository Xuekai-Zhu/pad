def solution():
    """The average score on last week's Spanish test was 90. Marco scored 10% less than the average test score and Margaret received 5 more points than Marco. What score did Margaret receive on her test?"""
    average_score = 90
    marco_score = 0.9 * average_score
    margaret_score = marco_score + 5
    result = margaret_score
    return result

print(solution())