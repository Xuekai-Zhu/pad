def solution():
    """Keith scored 3 points on the math test. Larry scored 3 times as many marks. Danny scored 5 more marks than Larry. Find the total amount of marks scored by the three students."""
    keith_marks = 3
    larry_marks = keith_marks * 3
    danny_marks = larry_marks + 5
    total_marks = keith_marks + larry_marks + danny_marks
    result = total_marks
    return result

print(solution())