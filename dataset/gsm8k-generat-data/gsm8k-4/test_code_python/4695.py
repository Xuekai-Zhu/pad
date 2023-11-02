def solution():
    """Nancy takes 3 antacids per day when she eats Indian food, 2 antacids per day when she eats Mexican food, and 1 antacid per day otherwise. 
    If Nancy eats Indian three times a week and Mexican twice a week, how many antacids does she take per month?"""
    
    # Define the number of days in a week and a month
    DAYS_IN_WEEK = 7
    DAYS_IN_MONTH = 30
    
    # Define the number of antacids taken for each type of food
    antacids_indian = 3
    antacids_mexican = 2
    antacids_other = 1
    
    # Calculate the number of antacids taken each week
    antacids_per_week = (antacids_indian * 3) + (antacids_mexican * 2) + (antacids_other * 2)
    
    # Calculate the number of antacids taken per month
    antacids_per_month = antacids_per_week * (DAYS_IN_MONTH / DAYS_IN_WEEK)
    
    result = antacids_per_month
    return result

print(solution())