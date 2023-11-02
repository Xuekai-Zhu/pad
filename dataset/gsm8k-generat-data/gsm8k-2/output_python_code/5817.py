def solution():
    """Tommy is looking at his change collection. He has 10 more dimes than pennies. He has twice as many nickels as dimes. He has 4 quarters. He has 10 times as many pennies as quarters. How many nickels does he have?"""
    quarters = 4
    pennies = 10 * quarters
    dimes = pennies + 10
    nickels = 2 * dimes
    result = nickels
    return result

print(solution())