def solution():
    # Define the variables
    cost_of_watch = 100
    weekly_allowance = 5
    initial_savings = 20

    # Calculate the amount of money Barbara can save per week
    savings_per_week = weekly_allowance

    # Calculate how many weeks Barbara needs to save up for the watch
    weeks_needed = (cost_of_watch - initial_savings) / savings_per_week

    result = weeks_needed
    return result

print(solution())