def solution():
    """Justin has a jar with many coins in it. The jar has 32 quarters, 95 dimes, 120 nickels, and 750 pennies. What is the total dollar amount in the jar?"""
    total_quarters = 32
    total_dimes = 95
    total_nickels = 120
    total_pennies = 750
    total_dollars = (total_quarters * 0.25) + (total_dimes * 0.1) + (total_nickels * 0.05) + (total_pennies * 0.01)
    result = total_dollars
    return result

print(solution())