def solution():
    num_bags = 2
    original_price = 6.0
    discount = 0.75  # 75% off

    # Calculate the discounted price of one bag
    discounted_price = original_price * (1 - discount)

    # Calculate the total cost of two bags at the discounted price
    total_cost = num_bags * discounted_price
    result = total_cost
    return result

print(solution())