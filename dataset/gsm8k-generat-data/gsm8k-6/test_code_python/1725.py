def solution():
    # Calculate the total cost of the MRI and x-ray
    xray_cost = 250
    mri_cost = 3 * xray_cost
    total_cost = xray_cost + mri_cost

    # Calculate the amount covered by insurance and the amount Mike paid out of pocket
    insurance_coverage = 0.8
    paid_by_insurance = total_cost * insurance_coverage
    paid_out_of_pocket = total_cost - paid_by_insurance

    result = paid_out_of_pocket
    return result

print(solution())