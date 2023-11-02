def solution():
    insurance_coverage = 80
    visit_cost = 300
    out_of_pocket_cost = visit_cost - (insurance_coverage / 100 * visit_cost)
    result = out_of_pocket_cost
    return result

print(solution())