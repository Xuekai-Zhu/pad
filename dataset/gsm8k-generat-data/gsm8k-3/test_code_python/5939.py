def solution():
    """William's class set a goal each week of the number of cans of food that is to be collected. On the first day, 20 cans were collected. Then the number of cans increased by 5 each day. If they collected 5 days a week to reach their goal, how many cans of food was their goal per week?"""
    # Define the number of days they collect cans
    days = 5

    # Define the starting number of cans
    start = 20

    # Define the increase in cans each day
    increase = 5

    # Calculate the goal for the week
    goal = start + (increase * (days - 1))

    # Display the goal for the week
    result = goal
    return result

print(solution())