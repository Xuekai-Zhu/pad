def solution():
    num_toys = 28
    toy_price = 10

    num_teddy_bears = 20

    total_cost = 580

    # Calculate the total cost of only the toys
    toy_cost_only = num_toys * toy_price

    # Calculate the cost of only the teddy bears
    teddy_bear_cost_only = total_cost - toy_cost_only

    # Calculate the cost per teddy bear
    teddy_bear_price = teddy_bear_cost_only / num_teddy_bears
    result = teddy_bear_price
    return result

print(solution())