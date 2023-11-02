def solution():
    """In a grocery store, Julia bought 2 pieces of Snickers and 3 packs of M&M's. If each piece of Snickers costs $1.5 and a pack of M&M's has the same cost as 2 Snickers, how much is Julia's change if she gave the cashier 2 $10 bills?"""
    snickers_cost = 1.5
    mms_cost = 3 * 2 * snickers_cost
    total_cost = 2 * snickers_cost + mms_cost
    money_given = 2 * 10
    change = money_given - total_cost
    result = change
    return result

print(solution())