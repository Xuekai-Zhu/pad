def solution():
    """A store is comparing their profits throughout the year. They had profits of $1,500 in the first quarter of the year, $3,000 in the third quarter, and $2,000 in the fourth quarter. If their annual profits are $8,000, how much profit, in dollars, did they make in the second quarter?"""
    annual_profit = 8000
    first_quarter_profit = 1500
    third_quarter_profit = 3000
    fourth_quarter_profit = 2000
    second_quarter_profit = annual_profit - first_quarter_profit - third_quarter_profit - fourth_quarter_profit
    result = second_quarter_profit
    return result

print(solution())