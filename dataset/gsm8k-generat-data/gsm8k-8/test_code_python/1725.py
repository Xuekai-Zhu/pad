def solution():
    # Define the cost of the x-ray and MRI
    x_ray_cost = 250
    mri_cost = 3 * x_ray_cost

    # Calculate the total cost before insurance
    total_cost = x_ray_cost + mri_cost

    # Calculate the amount covered by insurance
    insurance_coverage = 0.8 * total_cost

    # Calculate the amount Mike paid out of pocket
    amount_paid = total_cost - insurance_coverage
    result = amount_paid
    return result

print(solution())