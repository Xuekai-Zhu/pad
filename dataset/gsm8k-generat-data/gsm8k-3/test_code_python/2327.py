def solution():
    """John needs to get a new seeing-eye dog.  The adoption fee cost $150 for an untrained dog.  It then takes 12 weeks of training which costs $250 a week. After the training, she needs certification which costs $3000 but her insurance covers 90% of that.  What is her out-of-pocket cost?"""
    # Define the costs
    ADOPTION_FEE = 150
    WEEKLY_TRAINING_COST = 250
    CERTIFICATION_COST = 3000
    INSURANCE_COVERAGE = 0.9

    # Calculate the total cost of training
    training_cost = 12 * WEEKLY_TRAINING_COST

    # Calculate the total cost before insurance coverage
    total_cost_before_coverage = ADOPTION_FEE + training_cost + CERTIFICATION_COST

    # Calculate the amount covered by insurance
    amount_covered_by_insurance = CERTIFICATION_COST * INSURANCE_COVERAGE

    # Calculate the out-of-pocket cost
    out_of_pocket_cost = total_cost_before_coverage - amount_covered_by_insurance

    # Display the out-of-pocket cost
    result = out_of_pocket_cost
    return result

print(solution())