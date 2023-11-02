def solution():
    """Brendan makes $6/hour as a waiter. He's scheduled for 2 8-hour shifts and 1 12-hour shift this week. He also makes an average of $12 in tips each hour. Brendan is supposed to pay 20% of his income in taxes, but he only reports 1/3rd of his tips to the IRS. How much money does Brendan pay in taxes each week?"""
    
    # Define Brendan's hourly wage and hours worked for the week
    HOURLY_WAGE = 6
    SHIFT_LENGTH_1 = 8
    SHIFT_LENGTH_2 = 8
    SHIFT_LENGTH_3 = 12
    
    # Calculate Brendan's earnings for the week
    hourly_earnings = (SHIFT_LENGTH_1 + SHIFT_LENGTH_2 + SHIFT_LENGTH_3) * HOURLY_WAGE
    tip_earnings = (SHIFT_LENGTH_1 + SHIFT_LENGTH_2 + SHIFT_LENGTH_3) * 12
    reported_tips = tip_earnings / 3
    total_earnings = hourly_earnings + reported_tips
    
    # Calculate Brendan's taxes
    taxes = total_earnings * 0.2
    
    # Display the amount of taxes Brendan pays
    result = taxes
    return result

print(solution())