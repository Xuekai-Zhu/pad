def solution():
    """John ends up damaging his hearing aids. He needs to replace both of them. They cost $2500 each. Insurance covers 80% of the cost. How much does he personally have to pay?"""
    cost_per_aid = 2500
    insurance_coverage = 0.8
    personal_payment = cost_per_aid * (1 - insurance_coverage) * 2
    result = personal_payment
    return result

print(solution())