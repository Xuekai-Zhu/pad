def solution():
    """Jackson works 5 days a week going door-to-door collecting for charity. His goal is to raise $1000 for the week. He earned $300 on Monday and $40 on Tuesday. If he collects an average of $10 for every 4 houses he visits, how many houses will he have to visit on each of the remaining days of the week to meet his goal?"""
    # Define the total amount he has left to raise
    goal = 1000 - 300 - 40

    # Calculate the number of houses he needs to visit each day to meet his goal
    houses_per_day = (goal / 5) // 2.5

    # Multiply by 4 to convert to the number of houses he needs to visit in total
    total_houses = houses_per_day * 4

    # return the result
    result = total_houses
    return result

print(solution())