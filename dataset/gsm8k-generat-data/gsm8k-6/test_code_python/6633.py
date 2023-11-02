def solution():
    # Calculate the total cost of the pants before discount
    pants_cost_before_discount = 4 * 110.00

    # Calculate the total cost of the socks before discount
    socks_cost_before_discount = 2 * 60.00

    # Calculate the 30% discount on pants and socks
    pants_discount = 0.30 * pants_cost_before_discount
    socks_discount = 0.30 * socks_cost_before_discount

    # Find the total cost after the discount
    total_cost = (pants_cost_before_discount - pants_discount) + (socks_cost_before_discount - socks_discount)

    result = total_cost
    return result

print(solution())