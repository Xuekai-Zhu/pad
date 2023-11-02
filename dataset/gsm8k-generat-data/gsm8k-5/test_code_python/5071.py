def solution():
    starting_balance = 100  # The club has a balance of $100 million
    sale_proceeds = 2 * 10  # The club sells 2 players for $10 million each
    purchase_cost = 4 * 15  # The club buys 4 players for $15 million each

    # Calculate the final balance of the club
    final_balance = starting_balance + sale_proceeds - purchase_cost
    result = final_balance
    return result

print(solution())