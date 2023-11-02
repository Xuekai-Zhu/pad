def solution():
    # Calculate Leila's original savings
    sweater_cost = 20
    remaining_savings = sweater_cost / (1/4)  # Leila spent 3/4 of her savings on make-up, so she has 1/4 of her savings remaining
    original_savings = remaining_savings / (3/4)  # Leila spent 3/4 of her savings, so she has 1/4 of her savings remaining
    result = original_savings
    return result

print(solution())