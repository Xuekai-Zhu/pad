def solution():
    """Woody wants to buy a games console that costs $282. Woody already has $42 and receives an allowance of $24 every week. How many weeks will it take him to save the money he needs for the game console?"""
    # Define the cost of the games console
    console_cost = 282

    # Define the amount Woody already has and his weekly allowance
    starting_amount = 42
    weekly_allowance = 24

    # Initialize the number of weeks counter and the total amount saved
    weeks = 0
    total_saved = starting_amount

    # Add Woody's allowance to the total saved each week until he has enough to buy the console
    while total_saved < console_cost:
        weeks += 1
        total_saved += weekly_allowance
    
    # Return the number of weeks it took to save enough money
    result = weeks
    return result

print(solution())