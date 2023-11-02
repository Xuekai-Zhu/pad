def solution():
    """The teacher told the class that if they averaged at least 75% on their final exam, they could have a pizza party. Everyone took the exam on Monday, except for William, who was allowed to take it on Tuesday. If there are 30 people in the class, and the average before he took the test was a 74%, what score does he have to get to make sure they get to have a pizza party?"""
    total_students = 30
    current_avg = 74
    required_avg = 75
    sum_before_test = current_avg * total_students
    sum_after_test = required_avg * (total_students + 1)
    score_needed = sum_after_test - sum_before_test
    result = score_needed
    return result

print(solution())