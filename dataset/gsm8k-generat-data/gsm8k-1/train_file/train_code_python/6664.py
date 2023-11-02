def solution():
    """Tom finds 10 quarters, 3 dimes, and 4 nickels and 200 pennies. In dollars, how much money did he find?"""
    total_quarters = 10
    total_dimes = 3
    total_nickels = 4
    total_pennies = 200
    total_cents = (total_quarters * 25) + (total_dimes * 10) + (total_nickels * 5) + total_pennies
    total_dollars = total_cents / 100
    result = total_dollars
    return result

print(solution())