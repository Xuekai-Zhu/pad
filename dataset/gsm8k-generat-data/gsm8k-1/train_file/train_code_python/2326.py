def solution():
    """John needs to get a new seeing-eye dog. The adoption fee cost $150 for an untrained dog. It then takes 12 weeks of training which costs $250 a week. After the training, she needs certification which costs $3000 but her insurance covers 90% of that. What is her out-of-pocket cost?"""
    adoption_fee = 150
    training_cost = 250 * 12
    certification_cost = 3000 * 0.1  # 10% not covered by insurance
    out_of_pocket_cost = adoption_fee + training_cost + certification_cost
    result = out_of_pocket_cost
    return result

print(solution())