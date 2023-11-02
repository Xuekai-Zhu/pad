def solution():
    
    visit_cost = 300
    cast_cost = 200
    insurance_coverage = 0.6
    total_cost = visit_cost + cast_cost
    insurance_paid = total_cost * insurance_coverage
    out_of_pocket_cost = total_cost - insurance_paid
    result = out_of_pocket_cost
    return result

print(solution())