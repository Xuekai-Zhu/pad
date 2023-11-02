def solution():
    # Calculate the number of students who scored 100%
    scored_100 = (2/5) * 80

    # Calculate the number of students who did not score 100%
    did_not_score_100 = 80 - scored_100

    # Calculate the number of students who scored over 80%
    scored_over_80 = (50/100) * did_not_score_100

    # Calculate the number of students who failed
    failed = did_not_score_100 - scored_over_80

    result = failed
    return result

print(solution())