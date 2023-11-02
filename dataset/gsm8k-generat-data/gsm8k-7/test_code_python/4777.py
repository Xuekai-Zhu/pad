def solution():
    num_chairs = 8
    original_price = 20
    discount = 0.25
    additional_discount = 1/3

    # Calculate the discounted price of each chair
    discounted_price = original_price * (1 - discount)

    # Calculate the total cost of the first 5 chairs
    first_5_chairs_cost = original_price * 5 * (1 - discount)

    # Calculate the total cost of the remaining chairs after the 25% discount
    remaining_chairs_cost = (num_chairs - 5) * discounted_price

    # Calculate the additional discount for buying more than 5 chairs
    additional_discount_amount = additional_discount * remaining_chairs_cost

    # Calculate the total cost of all chairs with all discounts applied
    total_cost = first_5_chairs_cost + remaining_chairs_cost - additional_discount_amount
    result = total_cost
    return result

print(solution())