def solution():
    """Johnny makes his signature crab dish 40 times a day.  It uses 1.5 pounds of crab meat.  Crab meat sells for $8 per pound.  How much does he spend in a week if he is closed 3 days a week?"""
    # Define the number of times Johnny makes the crab dish per week
    dishes_per_day = 40
    dishes_per_week = dishes_per_day * 7

    # Define the amount of crab meat used per dish
    crab_per_dish = 1.5

    # Define the cost of crab meat per pound
    crab_price = 8

    # Calculate the total amount of crab meat used per week
    crab_per_week = crab_per_dish * dishes_per_week

    # Calculate the total cost of crab meat used per week
    crab_cost = crab_per_week * crab_price

    # Calculate the cost of crab meat used per week while closed 3 days
    closed_days = 3
    crab_cost_closed = crab_cost * (7 - closed_days) / 7

    # Display the total cost of crab meat used per week
    result = crab_cost_closed
    return result

print(solution())