def solution():
    total_paid = 20  # Janet paid $20
    total_change = 11  # Janet got $11 in change back
    cost_per_muffin = 0.75  # Each muffin costs 75 cents

    # Calculate the total cost of the muffins
    total_cost = total_paid - total_change
    # Calculate the number of muffins Janet bought
    num_muffins = total_cost / cost_per_muffin
    result = num_muffins
    return result

print(solution())