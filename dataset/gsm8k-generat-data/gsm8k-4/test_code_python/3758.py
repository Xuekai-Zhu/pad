def solution():
    """A store is comparing their profits throughout the year. They had profits of $1,500 in the first quarter of the year, $3,000 in the third quarter, and $2,000 in the fourth quarter. If their annual profits are $8,000, how much profit, in dollars, did they make in the second quarter?"""
    # Define the annual profits and the profits of the other three quarters
    annual_profit = 8000
    q1_profit = 1500
    q3_profit = 3000
    q4_profit = 2000

    # Calculate the profit of the second quarter
    q2_profit = annual_profit - q1_profit - q3_profit - q4_profit

    result = q2_profit
    return result

print(solution())