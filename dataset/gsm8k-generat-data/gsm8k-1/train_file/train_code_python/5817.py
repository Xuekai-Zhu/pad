def solution():
    """Tommy is looking at his change collection. He has 10 more dimes than pennies. He has twice as many nickels as dimes. He has 4 quarters. He has 10 times as many pennies as quarters. How many nickels does he have?"""
    num_quarters = 4
    num_pennies = num_quarters * 10
    num_dimes = num_pennies + 10
    num_nickels = num_dimes * 2
    result = num_nickels
    return result

print(solution())