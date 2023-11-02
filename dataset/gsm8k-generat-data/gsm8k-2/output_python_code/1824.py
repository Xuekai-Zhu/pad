def solution():
    """Tom's cat needs an expensive surgery. He has had pet insurance for 24 months that cost $20 per month. The procedure cost $5000 but the insurance covers all but 20% of this. How much money did he save by having insurance?"""
    insurance_cost = 20 * 24
    surgery_cost = 5000
    insurance_coverage = surgery_cost * 0.8
    total_cost = surgery_cost - insurance_coverage
    savings = total_cost - insurance_cost
    result = savings
    return result

print(solution())