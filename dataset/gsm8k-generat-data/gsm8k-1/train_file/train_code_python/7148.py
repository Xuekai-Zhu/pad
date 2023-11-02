def solution():
    """Hillary always buys the Wednesday, Thursday and Friday editions of the local newspaper for $0.50 each. On Sunday, she spends $2.00 to get that copy. How much does she spend on the newspaper over 8 weeks?"""
    weekday_cost = 0.5 * 3
    sunday_cost = 2.0
    papers_per_week = 4
    total_cost_per_week = weekday_cost + sunday_cost
    total_cost_per_8weeks = total_cost_per_week * 8
    result = total_cost_per_8weeks
    return result

print(solution())