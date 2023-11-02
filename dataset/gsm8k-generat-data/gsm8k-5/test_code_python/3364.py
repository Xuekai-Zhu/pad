def solution():
    regular_price = 50  # The regular price of the polo shirt is $50
    discount_percent = 0.4  # Zane gets a 40% discount on the polo shirts
    num_shirts = 2  # Zane purchases 2 polo shirts

    # Calculate the total cost of the polo shirts at the regular price
    total_regular_price = regular_price * num_shirts

    # Calculate the total discount that Zane gets
    total_discount = total_regular_price * discount_percent

    # Calculate the total cost of the polo shirts after the discount
    total_cost = total_regular_price - total_discount
    result = total_cost
    return result

print(solution())