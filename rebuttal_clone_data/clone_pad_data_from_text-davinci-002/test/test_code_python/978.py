def solution():
    xray_cost = 250
    mri_cost = xray_cost * 3
    insurance_coverage = 80
    total_cost = xray_cost + mri_cost
    insurance_payment = total_cost * (insurance_coverage / 100)
    mike_payment = total_cost - insurance_payment
    result = mike_payment
    
    return result

print(solution())