def solution():
    # Calculate the total cost of the t-shirts and bags
    total_cost = 2*8 + 2*10  # Timothy buys 2 t-shirts and 2 bags

    # Calculate the amount of money Timothy has left
    remaining_money = 50 - total_cost

    # Calculate the number of key chains Timothy can buy
    key_chains_price = 2/3  # $2 for 3 pieces of key chains
    key_chains_quantity = remaining_money // key_chains_price

    result = key_chains_quantity
    return result

print(solution())