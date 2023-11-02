def solution():
    """Woody wants to buy a games console that costs $282. Woody already has $42 and receives an allowance of $24 every week. How many weeks will it take him to save the money he needs for the game console?"""
    # Define the cost of the game console and Woody's current savings
    CONSOLE_COST = 282
    CURRENT_SAVINGS = 42

    # Define Woody's weekly allowance
    WEEKLY_ALLOWANCE = 24

    # Calculate how much Woody needs to save
    amount_to_save = CONSOLE_COST - CURRENT_SAVINGS

    # Calculate how many weeks it will take him to save that amount
    weeks_needed = amount_to_save // WEEKLY_ALLOWANCE

    # Display the number of weeks needed to save up
    result = weeks_needed
    return result

print(solution())