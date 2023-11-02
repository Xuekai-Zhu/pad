def solution():
    """Keith scored 3 points on the math test. Larry scored 3 times as many marks. Danny scored 5 more marks than Larry. Find the total amount of marks scored by the three students."""
    keith_score = 3
    larry_score = 3 * keith_score
    danny_score = larry_score + 5
    total_score = keith_score + larry_score + danny_score
    result = total_score
    return result

print(solution())