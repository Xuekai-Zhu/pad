def solution():
    """Paulo wants to get a burger meal that costs $6. Aside from that, he also wants to get a soda which costs 1/3 as much as the burger meal. While on the counter, Jeremy asked Paulo to get him 2 of each item Paulo is going to get. How much will they be charged for their orders combined?"""
    # Define the cost of the burger meal and the soda
    burger_cost = 6
    soda_cost = burger_cost / 3

    # Calculate the total cost for Paulo's order
    paulo_order_cost = burger_cost + soda_cost

    # Calculate the total cost for Jeremy's order
    jeremy_order_cost = 2 * (burger_cost + soda_cost)

    # Calculate the combined cost for both orders
    total_cost = paulo_order_cost + jeremy_order_cost

    result = total_cost
    return result

print(solution())