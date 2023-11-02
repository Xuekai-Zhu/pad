def solution():
    num_smart_tvs = 2
    tv_price = 650
    discount = 0.25  # 25% discount

    # Calculate the original total cost of the two smart televisions
    original_total_cost = num_smart_tvs * tv_price

    # Calculate the discounted total cost of the two smart televisions
    discounted_total_cost = original_total_cost * (1 - discount)

    result = discounted_total_cost
    return result

print(solution())