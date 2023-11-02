def solution():
    num_friends = 4
    original_price = 20
    discount = 0.5  # 50% off

    # Calculate the discounted price of the t-shirt
    discounted_price = original_price * (1 - discount)

    # Calculate the total cost for all four friends
    total_cost = num_friends * discounted_price
    result = total_cost
    return result

print(solution())