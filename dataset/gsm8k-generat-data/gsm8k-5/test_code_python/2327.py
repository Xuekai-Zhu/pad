def solution():
    # Calculate cost of adoption and training
    adoption_cost = 150
    training_cost = 12 * 250

    # Calculate cost of certification after insurance coverage
    certification_cost = 3000 * 0.1  # 90% insurance coverage
    total_cost = adoption_cost + training_cost + certification_cost
    result = total_cost
    return result

print(solution())