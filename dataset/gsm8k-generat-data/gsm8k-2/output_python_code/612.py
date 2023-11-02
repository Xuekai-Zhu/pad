def solution():
    """John ends up damaging his hearing aids. He needs to replace both of them. They cost $2500 each. Insurance covers 80% of the cost. How much does he personally have to pay?"""
    hearing_aid_cost = 2500
    insurance_coverage = 0.8
    total_cost = 2 * hearing_aid_cost
    insurance_paid = total_cost * insurance_coverage
    personal_cost = total_cost - insurance_paid
    result = personal_cost
    return result

print(solution())