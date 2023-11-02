def solution():
    """John goes to the market and buys 3 goats for $500 each and 2 cows for $1500 each. How much money did he spend?"""
    num_goats = 3
    goat_price = 500
    num_cows = 2
    cow_price = 1500
    total_spent = num_goats * goat_price + num_cows * cow_price
    result = total_spent
    return result

print(solution())