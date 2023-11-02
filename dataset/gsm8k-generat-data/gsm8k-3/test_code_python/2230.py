def solution():
    """Alfonso earns $6 each day walking his aunt’s dog. He is saving to buy a mountain bike helmet for $340. Currently, he already has $40. If he walks his aunt's dog 5 days a week, in how many weeks should Alfonso work to buy his mountain bike?"""
    # Define the amount Alfonso earns and his current savings
    DAILY_EARNINGS = 6
    CURRENT_SAVINGS = 40
    
    # Calculate the total amount Alfonso needs to save
    TOTAL_SAVINGS = 340 - CURRENT_SAVINGS
    
    # Calculate the number of days Alfonso needs to work
    total_days = TOTAL_SAVINGS / DAILY_EARNINGS
    
    # Convert the number of days to weeks
    weeks = total_days / 5
    
    # Display the number of weeks it will take for Alfonso to save for the helmet
    result = weeks
    return result

print(solution())