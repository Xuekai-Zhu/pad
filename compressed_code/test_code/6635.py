def solution():
    
    production_per_day = 10
    total_production_first_year = 365 * production_per_day
    production_reduction_percent = 10
    production_reduction_amount = total_production_first_year * (production_reduction_percent / 100)
    total_production_second_year = total_production_first_year - production_reduction_amount
    result = total_production_second_year
    return result

print(solution())