def solution():
    num_shirts = 6
    regular_price = 50
    discount = 0.2  # 20% discount

    # Calculate the discounted price per shirt
    discounted_price = regular_price * (1 - discount)

    # Calculate the total cost of all shirts
    total_cost = num_shirts * discounted_price

    result = total_cost
    return result

print(solution())