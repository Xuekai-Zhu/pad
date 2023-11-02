def solution():
    """A factory produced televisions at a constant rate of 10 per day in a certain year. If they reduced the total production by 10 percent in the second year, calculate the total production of television by the factory in the second year."""
    production_per_day = 10
    total_production_first_year = 365 * production_per_day
    production_reduction_percent = 10
    production_reduction_amount = total_production_first_year * (production_reduction_percent / 100)
    total_production_second_year = total_production_first_year - production_reduction_amount
    result = total_production_second_year
    return result

print(solution())