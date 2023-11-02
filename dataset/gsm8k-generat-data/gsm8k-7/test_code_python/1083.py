def solution():
    production_rate = 10 # TVs per day
    days_in_year = 365 # year assumed to have 365 days
    total_production_year1 = production_rate * days_in_year

    # Calculate the total production in year 2 after reducing it by 10%
    reduction_percent = 0.1 # 10% reduction
    total_production_year2 = total_production_year1 * (1 - reduction_percent)
    result = total_production_year2
    return result

print(solution())