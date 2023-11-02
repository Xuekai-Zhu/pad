def solution():
    """Nancy takes 3 antacids per day when she eats Indian food, 2 antacids per day when she eats Mexican food, and 1 antacid per day otherwise. If Nancy eats Indian three times a week and Mexican twice a week, how many antacids does she take per month?"""
    antacids_per_indian_meal = 3
    antacids_per_mexican_meal = 2
    antacids_per_regular_day = 1
    days_per_week = 7
    indian_days_per_week = 3
    mexican_days_per_week = 2
    regular_days_per_week = days_per_week - indian_days_per_week - mexican_days_per_week
    
    total_antacids = (antacids_per_indian_meal * indian_days_per_week) + (antacids_per_mexican_meal * mexican_days_per_week) + (antacids_per_regular_day * regular_days_per_week)
    antacids_per_month = total_antacids * 4
    result = antacids_per_month
    
    return result

print(solution())