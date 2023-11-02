def solution():
    """Paulo wants to get a burger meal that costs $6. Aside from that, he also wants to get a soda which costs 1/3 as much as the burger meal. While on the counter, Jeremy asked Paulo to get him 2 of each item Paulo is going to get. How much will they be charged for their orders combined?"""
    # Define the cost of the burger meal and soda
    BURGER_COST = 6
    SODA_COST = BURGER_COST / 3

    # Calculate the cost of Paulo's order
    paulo_order_cost = BURGER_COST + SODA_COST

    # Calculate the cost of Jeremy's order
    jeremy_order_cost = (BURGER_COST + SODA_COST) * 2

    # Calculate the total cost of both orders
    total_cost = paulo_order_cost + jeremy_order_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())