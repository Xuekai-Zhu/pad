def solution():
    total_money = 50  # Timothy has $50 to spend
    t_shirt_cost = 8  # T-shirts cost $8 each
    bag_cost = 10  # Bags cost $10 each

    # Calculate the cost of the t-shirts and bags Timothy buys
    total_cost = (2 * t_shirt_cost) + (2 * bag_cost)

    # Calculate the amount of money Timothy has left
    money_left = total_money - total_cost

    # Calculate how many key chain sets Timothy can buy with the money left
    key_chain_cost = 2/3  # 3 key chains cost $2, which means 1 key chain cost $2/3
    num_key_chain_sets = money_left // key_chain_cost

    result = num_key_chain_sets
    return result

print(solution())