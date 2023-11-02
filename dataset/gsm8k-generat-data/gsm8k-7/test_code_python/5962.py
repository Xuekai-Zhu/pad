def solution():
    t_shirt_price = 30
    backpack_price = 10
    blue_cap_price = 5
    total_paid = 43

    # Calculate the original price before discount
    original_price = t_shirt_price + backpack_price + blue_cap_price

    # Calculate the discount
    discount = original_price - total_paid
    result = discount
    return result

print(solution())