def solution():
    insurance_coverage = 80
    hearing_aid_cost = 2500
    insurance_payment = hearing_aid_cost * (insurance_coverage / 100)
    out_of_pocket_cost = hearing_aid_cost - insurance_payment
    total_cost = out_of_pocket_cost * 2
    result = total_cost
    
    return result

print(solution())