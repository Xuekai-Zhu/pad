def solution():
    """Tina makes $18.00 an hour. If she works more than 8 hours per shift, she is eligible for overtime, 
    which is paid by your hourly wage + 1/2 your hourly wage. If she works 10 hours every day for 5 days, 
    how much money does she make?"""
    
    # Define Tina's hourly wage and the number of hours worked per day and week
    hourly_wage = 18
    hours_per_day = 10
    days_per_week = 5
    
    # Calculate Tina's total earnings for a regular workday
    regular_earnings = hourly_wage * hours_per_day
    
    # Calculate Tina's overtime earnings for a workday
    overtime_hours = hours_per_day - 8
    overtime_earnings = (hourly_wage * 1.5) * overtime_hours
    
    # Calculate Tina's total earnings for a workday
    total_earnings = regular_earnings + overtime_earnings
    
    # Calculate Tina's total earnings for a week
    weekly_earnings = total_earnings * days_per_week
    
    result = weekly_earnings
    return result

print(solution())