def solution():
    
    insurance_cost = 20 * 24
    procedure_cost = 5000
    insurance_coverage = procedure_cost * 0.8
    total_cost_with_insurance = procedure_cost - insurance_coverage + insurance_cost
    total_cost_without_insurance = procedure_cost
    money_saved = total_cost_without_insurance - total_cost_with_insurance
    result = money_saved
    return result

print(solution())