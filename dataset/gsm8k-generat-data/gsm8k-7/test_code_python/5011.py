def solution():
    regular_price = 40.0
    discount = 0.25 # 25% off
    num_manipedis = 5

    # Calculate the discounted price of one mani/pedi
    discounted_price = regular_price * (1 - discount)

    # Calculate the total cost of all 5 mani/pedis
    total_cost = discounted_price * num_manipedis
    result = total_cost
    return result

print(solution())