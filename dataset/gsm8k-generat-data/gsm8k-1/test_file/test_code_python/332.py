def solution():
    """Maria buys 8 shares of a stock for $8 each. The stock price increases 50% the first year Maria holds it, then decreases 25% in the second year. What is the final value of all Maria's shares?"""
    num_shares = 8
    initial_price = 8
    first_year_increase = 0.5
    second_year_decrease = 0.25
    first_year_price = initial_price * (1 + first_year_increase)
    second_year_price = first_year_price * (1 - second_year_decrease)
    total_value = num_shares * second_year_price
    result = total_value
    return result

print(solution())