def solution():
    """Tom receives a $12 allowance per month. In the first week, he spends a third of it; in the second week, he spends a quarter of what he has left. How much money does he have left to finish the month?"""
    allowance = 12
    spent_first_week = allowance/3
    remaining1 = allowance - spent_first_week
    spent_second_week = remaining1/4
    remaining2 = remaining1 - spent_second_week
    result = remaining2
    return result

print(solution())