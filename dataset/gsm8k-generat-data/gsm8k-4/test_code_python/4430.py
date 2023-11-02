def solution():
    """Barbara wants to save up for a new wristwatch that costs $100. Her parents give her an allowance of $5 a week and she can either save it all up for the watch or spend it as she wishes. 10 weeks pass and due to spending some of her money on ice cream, Barbara currently only has $20. How many more weeks does she need to save for a watch if she stops spending on other things right now?"""
    # Define the cost of the watch and Barbara's current savings
    watch_cost = 100
    current_savings = 20

    # Define Barbara's weekly allowance and the number of weeks passed
    weekly_allowance = 5
    weeks_passed = 10

    # Calculate the total savings if Barbara stops spending on other things
    total_savings = current_savings + (weekly_allowance * (20 - weeks_passed))

    # Calculate the number of weeks needed to save for the watch
    weeks_needed = (watch_cost - total_savings) / weekly_allowance

    # Round up to the nearest integer
    result = int(weeks_needed + 1)
    return result

print(solution())