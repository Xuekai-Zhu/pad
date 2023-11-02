def solution():
    total_money = 50
    tshirt_price = 8
    bags_price = 10

    # Calculate the total cost of t-shirts and bags
    total_tshirt_cost = 2 * tshirt_price
    total_bags_cost = 2 * bags_price
    total_other_cost = total_tshirt_cost + total_bags_cost

    # Calculate the amount of money left
    money_left = total_money - total_other_cost

    # Calculate how many key chains Timothy can buy with the amount of money left
    key_chain_price = 2/3  # price of 1 key chain
    num_key_chains = money_left // key_chain_price  # integer division
    result = num_key_chains
    return result

print(solution())