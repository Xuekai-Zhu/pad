def solution():
    num_pants = 4
    pants_price = 110.0
    pants_discount = 0.3  # 30% discount

    num_socks = 2
    socks_price = 60.0
    socks_discount = 0.3

    # Calculate the total cost of all the pants before the discount
    total_pants_cost = num_pants * pants_price

    # Calculate the total cost of all the socks before the discount
    total_socks_cost = num_socks * socks_price

    # Calculate the discount for the pants
    pants_discount_amount = total_pants_cost * pants_discount

    # Calculate the discount for the socks
    socks_discount_amount = total_socks_cost * socks_discount

    # Calculate the total cost after the discount
    total_cost = total_pants_cost - pants_discount_amount + total_socks_cost - socks_discount_amount
    result = total_cost
    return result

print(solution())