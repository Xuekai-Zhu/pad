def solution():
    
    # Define Prince's hourly wage and number of hours worked per day
    HOURLY_WAGE = 15
    HOURS_WORKED_PER_DAY = 10

    # Define the weight of the bull
    BULL_WEIGHT = 750

    # Calculate Prince's daily earnings
    daily_earnings = HOURLY_WAGE * HOURS_WORKED_PER_DAY

    # Calculate the number of days it will take Prince to sell the meat
    days_to_sell = BULL_WEIGHT / daily_earnings

    # Display the number of days
    result = days_to_sell
    return result

print(solution())