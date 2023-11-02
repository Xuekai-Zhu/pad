def solution():
    """Jack has been driving for the past 9 years. He drives 37,000 miles every four months. How many miles has Jack driven since he started driving?"""
    years_driving = 9
    miles_per_four_months = 37000
    total_four_month_periods = years_driving * 3
    total_miles_driven = total_four_month_periods * miles_per_four_months
    result = total_miles_driven
    return result

print(solution())