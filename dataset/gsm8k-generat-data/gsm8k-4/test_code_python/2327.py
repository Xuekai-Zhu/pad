def solution():
    """John needs to get a new seeing-eye dog. The adoption fee cost $150 for an untrained dog. It then takes 12 weeks of training which costs $250 a week. After the training, she needs certification which costs $3000 but her insurance covers 90% of that. What is her out-of-pocket cost?"""
    
    # Calculate the cost of training
    training_cost = 250 * 12
    
    # Calculate the total cost before insurance coverage
    total_cost = 150 + training_cost + 3000
    
    # Calculate the insurance coverage
    insurance_coverage = 3000 * 0.9
    
    # Calculate the out-of-pocket cost
    out_of_pocket_cost = total_cost - insurance_coverage
    
    result = out_of_pocket_cost
    return result

print(solution())