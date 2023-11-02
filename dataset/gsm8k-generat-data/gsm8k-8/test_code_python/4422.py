def solution():
    # Calculate the original cost of 3 iPhones
    original_cost = 3 * 600

    # Calculate the cost with the 5% discount for buying 2 or more smartphones
    discount_cost = 0.95 * original_cost

    # Calculate the cost for each person if they buy individually
    individual_cost = 600

    # Calculate the total cost if they buy individually
    total_individual_cost = 3 * individual_cost

    # Calculate the amount saved by pooling their money and buying together
    amount_saved = total_individual_cost - discount_cost

    result = amount_saved
    return result

print(solution())