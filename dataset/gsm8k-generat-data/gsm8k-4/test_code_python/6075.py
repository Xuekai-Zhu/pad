def solution():
    """Tim hires two bodyguards. They each charge $20 an hour. He hires them for 8 hour per day. How much does he pay them in a week if he hires them 7 days a week?"""
    # Define the hourly rate for each bodyguard
    HOURLY_RATE = 20
    
    # Define the number of hours worked per day
    HOURS_PER_DAY = 8
    
    # Define the number of days worked per week
    DAYS_PER_WEEK = 7
    
    # Calculate the total cost for one bodyguard per day
    daily_cost = HOURLY_RATE * HOURS_PER_DAY * 2
    
    # Calculate the total cost for both bodyguards per week
    weekly_cost = daily_cost * DAYS_PER_WEEK
    
    result = weekly_cost
    return result

print(solution())