def solution():
    individual_cost = 10
    discount = 0.1  # 10% discount
    num_pairs = 3

    # Calculate the total cost of buying 3 pairs individually at different times
    total_individual_cost = individual_cost * num_pairs

    # Calculate the total cost of buying 3 pairs at once with discount
    total_discounted_cost = (individual_cost * num_pairs) * (1 - discount)

    # Calculate the amount saved by buying 3 pairs at once with discount
    amount_saved = total_individual_cost - total_discounted_cost
    result = amount_saved
    return result

print(solution())