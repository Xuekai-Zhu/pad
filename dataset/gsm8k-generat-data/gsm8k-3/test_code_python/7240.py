def solution():
    """Roberto is raising chickens for eggs. He buys 4 chickens for $20 each. They cost $1 in total a week to feed and each produces 3 eggs a week that will last forever. He used to buy 1 dozen eggs a week and spent $2 per dozen. After how many weeks will the chickens be cheaper than buying his eggs?"""
    # Define the initial cost of buying 4 chickens
    INITIAL_CHICKEN_COST = 20 * 4

    # Define the cost of buying 1 dozen eggs per week
    WEEKLY_EGG_COST = 2

    # Define the number of eggs produced by each chicken per week
    EGGS_PER_CHICKEN_PER_WEEK = 3

    # Define the number of weeks it will take for the chicken investment to pay off
    weeks = INITIAL_CHICKEN_COST / (EGGS_PER_CHICKEN_PER_WEEK * 12 - WEEKLY_EGG_COST * 12)

    # Display the number of weeks
    result = weeks
    return result

print(solution())