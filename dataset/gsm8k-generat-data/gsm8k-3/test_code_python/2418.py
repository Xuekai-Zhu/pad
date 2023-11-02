def solution():
    """Lyra has an $80 budget for a week to spend on food. If she bought 1 bucket of fried chicken that costs $12 and 5 pounds of beef that cost $3 per pound. How much is left on her weekly budget?"""
    # Define the cost of the bucket of fried chicken and the cost per pound of beef
    CHICKEN_COST = 12
    BEEF_COST_PER_POUND = 3

    # Define the amount of chicken and beef Lyra bought
    chicken_amount = 1
    beef_amount = 5

    # Calculate the total cost of the chicken
    chicken_cost = chicken_amount * CHICKEN_COST

    # Calculate the total cost of the beef
    beef_cost = beef_amount * BEEF_COST_PER_POUND

    # Calculate the total cost of all the food
    total_cost = chicken_cost + beef_cost

    # Calculate the amount left on her weekly budget
    remaining_budget = 80 - total_cost

    # Display the remaining budget
    result = remaining_budget
    return result

print(solution())