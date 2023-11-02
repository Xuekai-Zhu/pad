def solution():
    x_ray_cost = 250
    mri_cost = 3 * x_ray_cost
    insurance_coverage = 0.8

    # Calculate the total cost before insurance coverage
    total_cost_before_coverage = x_ray_cost + mri_cost

    # Calculate the amount covered by insurance
    amount_covered_by_insurance = total_cost_before_coverage * insurance_coverage

    # Calculate the amount paid by Mike
    amount_paid_by_mike = total_cost_before_coverage - amount_covered_by_insurance
    result = amount_paid_by_mike
    return result

print(solution())