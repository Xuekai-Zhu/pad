def solution():
    starting_money = 20
    num_sock_pairs = 4
    sock_pair_price = 2
    hat_price = 7

    # Calculate the total cost of all sock pairs
    total_sock_pair_cost = num_sock_pairs * sock_pair_price

    # Calculate the total cost of all items purchased
    total_cost = total_sock_pair_cost + hat_price

    # Calculate the remaining money after purchase
    remaining_money = starting_money - total_cost
    result = remaining_money
    return result

print(solution())