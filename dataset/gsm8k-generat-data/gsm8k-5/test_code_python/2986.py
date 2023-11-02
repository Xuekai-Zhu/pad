def solution():
    cost_per_phone = 800  # Each cellphone costs $800
    discount_rate = 0.05  # Miley gets a 5% discount for buying two phones
    total_cost = 2 * cost_per_phone  # Total cost before discount
    discount_amount = discount_rate * total_cost  # Amount of discount
    discounted_total = total_cost - discount_amount  # Total cost after discount
    result = discounted_total
    return result

print(solution())