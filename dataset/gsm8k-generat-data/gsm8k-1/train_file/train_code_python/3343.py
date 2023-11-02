def solution():
    """A jar on the family's counter contains change they've been saving for a trip to the ice cream shop. There are 123 pennies, 85 nickels, 35 dimes, and a number of quarters. All five family members get a double scoop, which costs $3 each. After the trip, they have 48 cents left over. How many quarters were in the jar?"""
    pennies = 0.01 * 123
    nickels = 0.05 * 85
    dimes = 0.10 * 35
    total_change = pennies + nickels + dimes + 0.25 * x
    total_cost = 5 * 3
    leftover = 0.48
    x = int((leftover + total_cost - total_change) / 0.25)
    result = x
    return result

print(solution())