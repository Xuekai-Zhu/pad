def solution():
    cost_per_epipen = 500
    insurance_coverage = 0.75
    num_epipens_per_year = 2

    # Calculate the cost of one EpiPen after insurance coverage
    cost_after_insurance = cost_per_epipen * (1 - insurance_coverage)

    # Calculate the total cost of two EpiPens per year
    total_cost_per_year = num_epipens_per_year * cost_after_insurance

    result = total_cost_per_year
    return result

print(solution())