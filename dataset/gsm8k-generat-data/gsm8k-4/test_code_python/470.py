def solution():
    """A lot of people have been sick at Gary's workplace, so he's been working a lot of extra shifts to fill in for people. As a result, he's earned some overtime (where every hour after 40 he earns 1.5 times his normal wage.) His paycheck (before taxes are taken out) came out to $696. If Gary normally earns $12 per hour, how many hours did he work that week?"""
    # Define the normal wage and the overtime pay rate
    WAGE_PER_HOUR = 12
    OVERTIME_PAY_RATE = 1.5

    # Define the number of hours worked and the overtime hours worked
    hours_worked = 0
    overtime_hours = 0

    # Calculate the overtime hours worked and the regular hours worked
    if 696 >= 40 * WAGE_PER_HOUR:
        overtime_hours = (696 - 40 * WAGE_PER_HOUR) / (WAGE_PER_HOUR * OVERTIME_PAY_RATE - WAGE_PER_HOUR)  
        hours_worked = 40 + overtime_hours      
    else:
        hours_worked = 696 / WAGE_PER_HOUR
    
    result = round(hours_worked,2)
    return result

print(solution())