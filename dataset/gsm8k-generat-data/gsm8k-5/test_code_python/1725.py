def solution():
    x_ray_cost = 250
    mri_cost = 3 * x_ray_cost  # MRI cost is triple the X-ray cost
    total_cost = x_ray_cost + mri_cost  # Total cost for both procedures
    insurance_coverage = 0.8  # Insurance covers 80% of the total cost

    # Calculate the amount Mike paid
    amount_paid = total_cost * (1 - insurance_coverage)
    result = amount_paid
    return result

print(solution())