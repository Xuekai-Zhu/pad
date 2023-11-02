def solution():
    cost_per_pair = 10  # Each pair of shorts costs $10
    discount_percent = 10  # The discount is 10%
    num_pairs = 3  # Stacy wants to buy 3 pairs

    # Calculate the total cost of buying 3 pairs at once, with discount
    total_cost_with_discount = num_pairs * cost_per_pair * (1 - discount_percent/100)

    # Calculate the total cost of buying 3 pairs individually, without discount
    total_cost_without_discount = num_pairs * cost_per_pair

    # Calculate the amount saved by buying 3 pairs at once
    amount_saved = total_cost_without_discount - total_cost_with_discount
    result = amount_saved
    return result

print(solution())