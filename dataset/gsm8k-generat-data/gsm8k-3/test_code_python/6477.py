def solution():
    """Jackson works 5 days a week going door-to-door collecting for charity. His goal is to raise $1000 for the week. He earned $300 on Monday and $40 on Tuesday. If he collects an average of $10 for every 4 houses he visits, how many houses will he have to visit on each of the remaining days of the week to meet his goal?"""
    # Define the number of days, total goal, and amount already collected
    days = 5
    total_goal = 1000
    collected = 300 + 40

    # Calculate the remaining amount to be collected
    remaining = total_goal - collected

    # Calculate the average amount collected per 4 houses
    per_house = 10

    # Calculate the number of houses to visit each day to meet the goal
    houses_per_day = (remaining / (days - 2)) / (per_house / 4)

    # Display the number of houses to visit per day
    result = houses_per_day
    return result

print(solution())