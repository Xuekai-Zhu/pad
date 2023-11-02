def solution():
    # Calculate the price of one t-shirt after the discount
    discounted_price = 20 * 0.5  # 50% discount
    final_price = 20 - discounted_price  # original price minus the discount

    # Calculate the total money spent by all four friends
    total_spent = 4 * final_price

    result = total_spent
    return result

print(solution())