def solution():
    """Ursula earns $8.50 an hour working in a restaurant. She works 8 hours a day. If she works 20 days a month, determine her annual salary."""
    # Define Ursula's hourly wage and daily working hours
    HOURLY_WAGE = 8.50
    DAILY_HOURS = 8
    
    # Define the number of working days in a month and a year
    MONTHLY_DAYS = 20
    YEARLY_DAYS = 12 * MONTHLY_DAYS
    
    # Calculate Ursula's monthly and yearly salary
    monthly_salary = HOURLY_WAGE * DAILY_HOURS * MONTHLY_DAYS
    yearly_salary = monthly_salary * 12
    
    # Display Ursula's yearly salary
    result = yearly_salary
    return result

print(solution())