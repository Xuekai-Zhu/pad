def solution():
    # Calculate the total cost of getting a new seeing-eye dog
    adoption_fee = 150
    training_cost = 250 * 12
    certification_cost = 3000 * 0.1  # 90% of the cost is covered by insurance
    total_cost = adoption_fee + training_cost + certification_cost
    out_of_pocket_cost = total_cost - (certification_cost * 0.9)
    result = out_of_pocket_cost
    return result

print(solution())