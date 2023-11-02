def solution():
    num_tshirts = 6
    full_price = 20.0
    discount = 0.5  # 50% off

    # Calculate the total cost without discount
    full_price_total = num_tshirts * full_price

    # Calculate the total discount
    total_discount = full_price_total * discount

    # Calculate the total cost with discount
    total_cost = full_price_total - total_discount
    result = total_cost
    return result

print(solution())