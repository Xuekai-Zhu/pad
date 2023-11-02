def solution():
    """Colby wants to buy some gumballs that cost a nickel each. If he has 8 quarters, 6 dimes, 14 nickels, and 15 pennies, how many can he buy?"""
    quarters = 8
    dimes = 6
    nickels = 14
    pennies = 15
    total_money = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
    gumball_cost = 5
    gumballs = total_money // gumball_cost
    result = gumballs
    return result

print(solution())