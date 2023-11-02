def solution():
    """James likes to check the coin return of the vending machine for change. One day he finds a quarter, two nickels, and 7 dimes. How much money in cents does James have?"""
    quarter_value = 25
    nickel_value = 5
    dime_value = 10
    quarter_count = 1
    nickel_count = 2
    dime_count = 7
    total_money = (quarter_count * quarter_value) + (nickel_count * nickel_value) + (dime_count * dime_value)
    result = total_money
    return result

print(solution())