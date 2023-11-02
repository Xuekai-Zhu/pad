def solution():
    """Buffy and Oz went to dinner.  They shared an appetizer that cost $9.00.  Each of their entrees was $20.00 and they shared a dessert that was $11.00.  If they left a 30% tip, what was the entire price of the meal?"""
    # Define the cost of each item
    APPETIZER_COST = 9
    ENTREE_COST = 20
    DESSERT_COST = 11

    # Calculate the total cost of food
    food_cost = APPETIZER_COST + 2 * ENTREE_COST + DESSERT_COST

    # Calculate the tip amount
    tip_amount = 0.3 * food_cost

    # Calculate the total cost of the meal
    total_cost = food_cost + tip_amount

    # Display the total cost
    result = total_cost
    return result

print(solution())