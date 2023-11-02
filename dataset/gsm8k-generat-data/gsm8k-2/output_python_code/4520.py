def solution():
    """John gets a new EpiPen every 6 months. They cost $500 and insurance covers 75%. How much does he pay per year?"""
    cost_per_epipen = 500
    insurance_coverage = 0.75
    num_epipens_per_year = 2
    total_cost_per_year = cost_per_epipen * num_epipens_per_year * (1 - insurance_coverage)
    result = total_cost_per_year
    return result

print(solution())