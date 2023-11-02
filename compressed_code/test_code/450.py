def solution():
    
    hearing_aid_cost = 2500
    insurance_coverage = 0.8
    total_cost = 2 * hearing_aid_cost
    insurance_paid = total_cost * insurance_coverage
    personal_cost = total_cost - insurance_paid
    result = personal_cost
    return result

print(solution())