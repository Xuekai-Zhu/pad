def solution():
    """A football club has a balance of $100 million. The club then sells 2 of its players at $10 million each, and buys 4 more at $15 million each. How much money is left in the club register in millions of dollars?"""
    initial_balance = 100
    sell_price = 10
    buy_price = 15
    players_sold = 2
    players_bought = 4
   
    remaining_balance = (initial_balance - (sell_price * players_sold) + (buy_price * players_bought))
    result = remaining_balance
    return result

print(solution())