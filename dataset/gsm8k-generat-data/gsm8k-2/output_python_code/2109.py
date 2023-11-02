def solution():
    """In a grocery store, Julia bought 2 pieces of Snickers and 3 packs of M&M's. If each piece of Snickers costs $1.5 and a pack of M&M's has the same cost as 2 Snickers, how much is Julia's change if she gave the cashier 2 $10 bills?"""
    snickers_price = 1.5
    mms_price = 3 * snickers_price
    total_cost = (2 * snickers_price) + mms_price
    cash_given = 20
    change = cash_given - total_cost
    result = change
    return result

print(solution())