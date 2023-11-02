def solution():
    """Kendall is counting her change. She has a total of $4 in quarters, dimes, and nickels. If she has 10 quarters and 12 dimes, how many nickels does she have?"""
    total_change = 4
    quarter_value = 0.25
    dime_value = 0.1
    nickel_value = 0.05
    quarter_count = 10
    dime_count = 12
    total_quarter_value = quarter_count * quarter_value
    total_dime_value = dime_count * dime_value
    total_nickel_value = total_change - total_quarter_value - total_dime_value
    nickel_count = int(total_nickel_value / nickel_value)
    result = nickel_count
    return result

print(solution())