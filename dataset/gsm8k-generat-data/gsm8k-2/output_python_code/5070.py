def solution():
    """A football club has a balance of $100 million. The club then sells 2 of its players at $10 million each, and buys 4 more at $15 million each. How much money is left in the club register in millions of dollars?"""
    starting_balance = 100
    sold_players = 2 * 10
    bought_players = 4 * 15
    ending_balance = starting_balance - sold_players + bought_players
    result = ending_balance
    return result

print(solution())