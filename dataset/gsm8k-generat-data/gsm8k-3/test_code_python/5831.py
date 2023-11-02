def solution():
    """When Herman’s team is busy working on large projects he stops at the drive-through 5 days, every week to buy a breakfast combo for himself and 3 members of his team.  Each meal costs $4.00.  This current project will last 16 weeks.  How much will Herman spend on breakfast?"""
    # Define the number of meals purchased per week and the cost per meal
    NUM_MEALS_PER_WEEK = 4
    MEAL_COST = 4

    # Define the number of weeks for the project
    NUM_WEEKS = 16

    # Calculate the total number of meals purchased
    total_meals = NUM_MEALS_PER_WEEK * NUM_WEEKS

    # Calculate the total cost of the meals
    total_cost = total_meals * MEAL_COST

    # Display the total cost of the meals
    result = total_cost
    return result

print(solution())