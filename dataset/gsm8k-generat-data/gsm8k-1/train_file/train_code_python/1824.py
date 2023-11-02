def solution():
    """Tom's cat needs an expensive surgery. He has had pet insurance for 24 months that cost $20 per month. The procedure cost $5000 but the insurance covers all but 20% of this. How much money did he save by having insurance?"""
    insurance_cost = 20 * 24
    procedure_cost = 5000
    insurance_coverage = procedure_cost * 0.8
    total_cost_with_insurance = procedure_cost - insurance_coverage + insurance_cost
    total_cost_without_insurance = procedure_cost
    money_saved = total_cost_without_insurance - total_cost_with_insurance
    result = money_saved
    return result

print(solution())