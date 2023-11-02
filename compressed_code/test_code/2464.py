def solution():
    
    months_per_year = 12
    growth_per_month = 0.5
    height_before_cutting = 4
    height_after_cutting = 2

    months_between_cuttings = (height_before_cutting - height_after_cutting) / growth_per_month
    total_cuttings_per_year = months_per_year / months_between_cuttings
    cost_per_cutting = 100
    total_cost_per_year = total_cuttings_per_year * cost_per_cutting

    result = total_cost_per_year
    return result

print(solution())