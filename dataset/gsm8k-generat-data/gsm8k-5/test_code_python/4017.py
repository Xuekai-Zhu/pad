def solution():
    visit_cost = 300
    cast_cost = 200
    total_cost = visit_cost + cast_cost

    insurance_coverage = 0.6
    covered_cost = total_cost * insurance_coverage

    out_of_pocket_cost = total_cost - covered_cost
    result = out_of_pocket_cost
    return result

print(solution())