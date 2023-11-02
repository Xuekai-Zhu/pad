def solution():
    adoption_fee = 150
    training_cost_per_week = 250
    num_weeks_training = 12
    certification_cost = 3000
    insurance_coverage = 0.9

    # Calculate total cost of training
    total_training_cost = training_cost_per_week * num_weeks_training

    # Calculate cost of certification after insurance coverage
    certification_out_of_pocket = (1 - insurance_coverage) * certification_cost

    # Calculate total out of pocket cost
    total_out_of_pocket_cost = adoption_fee + total_training_cost + certification_out_of_pocket
    result = total_out_of_pocket_cost
    return result

print(solution())