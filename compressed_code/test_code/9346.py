def solution():
    
    cost_per_epipen = 500
    insurance_coverage = 0.75
    num_epipens_per_year = 2
    total_cost = num_epipens_per_year * cost_per_epipen * (1 - insurance_coverage)
    result = total_cost
    return result

print(solution())