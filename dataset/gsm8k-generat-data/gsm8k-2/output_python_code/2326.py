def solution():
    """John needs to get a new seeing-eye dog. The adoption fee cost $150 for an untrained dog. It then takes 12 weeks of training which costs $250 a week. After the training, she needs certification which costs $3000 but her insurance covers 90% of that. What is her out-of-pocket cost?"""
    adoption_fee = 150
    training_cost = 12 * 250
    certification_cost = 3000 * 0.1
    total_cost = adoption_fee + training_cost + certification_cost
    result = total_cost
    return result

print(solution())