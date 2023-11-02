def solution():
    cost_per_set = 6  # Each set costs $6
    num_sets = 5  # The guy bought 5 sets
    subtotal = cost_per_set * num_sets  # Calculate the subtotal

    tax_rate = 0.1  # The tax rate is 10%
    total_tax = tax_rate * subtotal  # Calculate the total tax

    total_cost = subtotal + total_tax  # Calculate the total amount paid
    result = total_cost
    return result

print(solution())