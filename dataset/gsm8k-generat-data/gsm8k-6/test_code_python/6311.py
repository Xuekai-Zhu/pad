def solution():
    # Calculate the total cost of Thomas's order
    shirts_cost = 3 * 12
    socks_cost = 5
    shorts_cost = 2 * 15
    swim_trunks_cost = 14
    total_cost = shirts_cost + socks_cost + shorts_cost + swim_trunks_cost

    # Calculate the shipping cost based on the total cost of the order
    if total_cost < 50:
        shipping_cost = 5
    else:
        shipping_cost = 0.2 * total_cost

    # Calculate the total bill, including shipping
    total_bill = total_cost + shipping_cost
    result = total_bill
    return result

print(solution())