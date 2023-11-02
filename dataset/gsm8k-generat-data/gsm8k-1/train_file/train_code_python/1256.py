def solution():
    """Alice and Bob are each given $2000 to invest. Alice puts all of her money in the stock market and doubles her money. Bob invests in real estate and makes five times more money than he invested. How much more money does Bob have now than Alice?"""
    initial_investment = 2000
    alice_return = initial_investment * 2
    bob_return = initial_investment * 5
    difference = bob_return - alice_return
    result = difference
    return result

print(solution())