def solution():
    """Mike has to get an x-ray and an MRI. The x-ray is $250 and the MRI is triple that cost. Insurance covers 80%. How much did he pay?"""
    xray_cost = 250
    mri_cost = 3 * xray_cost
    total_cost = xray_cost + mri_cost
    insurance_coverage = 0.8
    amount_paid = total_cost * (1 - insurance_coverage)
    result = amount_paid
    return result

print(solution())