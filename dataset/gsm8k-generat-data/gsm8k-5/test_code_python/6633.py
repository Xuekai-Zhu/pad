def solution():
    # Calculate the cost of 4 pairs of pants after the discount
    pants_cost = 110.00 * 4
    pants_discount = pants_cost * 0.30
    total_pants_cost = pants_cost - pants_discount

    # Calculate the cost of 2 pairs of socks after the discount
    socks_cost = 60.00 * 2
    socks_discount = socks_cost * 0.30
    total_socks_cost = socks_cost - socks_discount

    # Calculate the total cost after the discount
    total_cost = total_pants_cost + total_socks_cost
    result = total_cost
    return result

print(solution())