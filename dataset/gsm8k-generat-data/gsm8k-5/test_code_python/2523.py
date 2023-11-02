def solution():
    initial_cost = 10000  # Jim buys a wedding ring for $10,000
    second_ring_cost = 2 * initial_cost  # Jim buys a ring that is twice as much

    # Jim sells the first ring for half its value
    first_ring_sell_price = 0.5 * initial_cost

    # Calculate the total cost for Jim
    total_cost = initial_cost + second_ring_cost - first_ring_sell_price
    result = total_cost
    return result

print(solution())