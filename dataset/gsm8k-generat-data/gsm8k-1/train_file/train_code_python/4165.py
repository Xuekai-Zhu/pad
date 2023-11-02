def solution():
    """A dime has the same value as 10 pennies and a nickel has the same value as 5 pennies. How many pennies will Grace have by exchanging her 10 dimes and 10 nickels?"""
    dimes = 10
    nickels = 10
    pennies_from_dimes = dimes * 10
    pennies_from_nickels = nickels * 5
    total_pennies = pennies_from_dimes + pennies_from_nickels
    result = total_pennies
    return result

print(solution())