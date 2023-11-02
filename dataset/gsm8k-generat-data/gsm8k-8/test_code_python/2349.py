def solution():
    # Define the cost of the burger meal and the soda
    burger_cost = 6
    soda_cost = burger_cost / 3

    # Calculate the total cost of Paulo's order
    paulo_order_cost = burger_cost + soda_cost

    # Calculate the total cost of Jeremy's order
    jeremy_order_cost = 2 * paulo_order_cost

    # Calculate the combined total cost
    combined_cost = paulo_order_cost + jeremy_order_cost
    result = combined_cost
    return result

print(solution())