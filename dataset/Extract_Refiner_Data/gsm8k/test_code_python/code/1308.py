def solution():
    
    # Define the number of reservations and the cost of each meal and wine
    RESERVINGS = 6
    MEAL_COST = 5
    WINE_COST = 5

    # Define the number of days Tom is open per week
    DAYS_PER_WEEK = 2

    # Calculate the total cost of meals per week
    meals_cost_per_week = RESERVINGS * 2 * MEAL_COST * DAYS_PER_WEEK

    # Calculate the total cost of wine per week
    wine_cost_per_week = WINE_COST * DAYS_PER_WEEK

    # Calculate the total cost of all reservations per week
    total_cost_per_week = meals_cost_per_week + wine_cost_per_week

    # Display the total cost per week
    result = total_cost_per_week
    return result

print(solution())