def solution():
    """Brenda invested $300 into a scheme that accumulates simple interest at the rate of three-quarters of the original amount per year. How much in total will she have after 3 years?"""
    initial_investment = 300
    interest_rate = 0.75
    years = 3
    total_amount = initial_investment + (initial_investment * interest_rate * years)
    result = total_amount
    return result

print(solution())