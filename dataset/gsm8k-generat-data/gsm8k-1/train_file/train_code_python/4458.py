def solution():
    """Kendall is counting her change. She has a total of $4 in quarters, dimes, and nickels. If she has 10 quarters and 12 dimes, how many nickels does she have?"""
    total_change = 4
    quarter_value = 0.25
    dime_value = 0.1
    nickel_value = 0.05
    quarters = 10
    dimes = 12
    quarter_amount = quarter_value * quarters
    dime_amount = dime_value * dimes
    remaining_amount = total_change - quarter_amount - dime_amount
    nickel_amount = int(remaining_amount / nickel_value)
    result = nickel_amount
    return result

print(solution())