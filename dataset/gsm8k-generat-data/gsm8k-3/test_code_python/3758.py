def solution():
    """A store is comparing their profits throughout the year. They had profits of $1,500 in the first quarter of the year, $3,000 in the third quarter, and $2,000 in the fourth quarter. If their annual profits are $8,000, how much profit, in dollars, did they make in the second quarter?"""
    # Calculate the total profits in the first, third and fourth quarters
    total_profit = 1500 + 3000 + 2000

    # Calculate the profit in the second quarter
    profit_2 = 8000 - total_profit

    # Display the profit in the second quarter
    result = profit_2
    return result

print(solution())