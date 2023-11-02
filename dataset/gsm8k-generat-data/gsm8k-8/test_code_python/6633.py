def solution():
    # Calculate the cost of the pants before the discount
    pants_cost = 4 * 110

    # Calculate the discount on the pants
    pants_discount = pants_cost * 0.3

    # Calculate the cost of the pants after the discount
    pants_final_cost = pants_cost - pants_discount

    # Calculate the cost of the socks before the discount
    socks_cost = 2 * 60

    # Calculate the discount on the socks
    socks_discount = socks_cost * 0.3

    # Calculate the cost of the socks after the discount
    socks_final_cost = socks_cost - socks_discount

    # Calculate the total cost after the discount
    total_cost = pants_final_cost + socks_final_cost

    result = total_cost
    return result

print(solution())