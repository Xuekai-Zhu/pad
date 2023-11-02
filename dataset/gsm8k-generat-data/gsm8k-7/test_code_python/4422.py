def solution():
    num_phones = 3
    phone_price = 600
    discount_percent = 5
    min_num_phones = 2

    # Calculate the total cost of buying the phones individually
    individual_cost = num_phones * phone_price

    # Calculate the cost of buying the phones together with the discount
    if num_phones >= min_num_phones:
        discounted_price = phone_price - (phone_price * discount_percent / 100)
        total_cost_discounted = num_phones * discounted_price
    else:
        total_cost_discounted = individual_cost

    # Calculate the amount saved by buying the phones together with the discount
    amount_saved = individual_cost - total_cost_discounted
    result = amount_saved
    return result

print(solution())