def solution():
    initial_balance = 100  # initial balance in millions of dollars
    sold_players = 2 * 10  # amount received from selling 2 players at $10 million each
    bought_players = 4 * 15  # amount spent on buying 4 players at $15 million each
    remaining_balance = initial_balance + sold_players - bought_players  # balance remaining after transactions
    result = remaining_balance
    return result

print(solution())