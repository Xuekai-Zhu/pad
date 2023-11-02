def solution():
    """A dime has the same value as 10 pennies and a nickel has the same value as 5 pennies. How many pennies will Grace have by exchanging her 10 dimes and 10 nickels?"""
    dimes_value = 10 * 10 # 100 pennies
    nickels_value = 10 * 5 # 50 pennies
    total_value = dimes_value + nickels_value # 150 pennies
    result = total_value
    return result

print(solution())