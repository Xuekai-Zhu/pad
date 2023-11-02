def solution():
    adoption_fee = 150
    weekly_training_cost = 250
    certification_cost = 3000
    insurance_coverage = 0.90
    total_cost = adoption_fee + (weekly_training_cost * 12) + (certification_cost * (1 - insurance_coverage))
    result = total_cost
    return result

print(solution())