def solution():
    # Calculate the number of students who scored 100%
    scored_100_percent = (2/5) * 80

    # Calculate the number of students who didn't score 100%
    didnt_score_100_percent = 80 - scored_100_percent

    # Calculate the number of students who scored over 80%
    scored_over_80_percent = 0.5 * didnt_score_100_percent

    # Calculate the number of students who failed
    failed_students = 80 - scored_100_percent - scored_over_80_percent

    result = failed_students
    return result

print(solution())