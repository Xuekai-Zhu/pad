def solution():
    """Barbara wants to save up for a new wristwatch that costs $100. Her parents give her an allowance of $5 a week and she can either save it all up for the watch or spend it as she wishes. 10 weeks pass and due to spending some of her money on ice cream, Barbara currently only has $20. How many more weeks does she need to save for a watch if she stops spending on other things right now?"""
    # Define the cost of the wristwatch and Barbara's allowance
    WATCH_COST = 100
    ALLOWANCE = 5

    # Define Barbara's current savings and the number of weeks passed
    current_savings = 20
    weeks_passed = 10

    # Calculate the amount Barbara can save each week
    weekly_savings = ALLOWANCE

    # Calculate the number of weeks needed to save for the watch
    remaining_cost = WATCH_COST - current_savings
    remaining_weeks = remaining_cost / weekly_savings

    # Display the number of weeks needed
    result = remaining_weeks
    return result

print(solution())