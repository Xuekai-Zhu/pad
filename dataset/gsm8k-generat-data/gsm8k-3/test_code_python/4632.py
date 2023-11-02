def solution():
    """Julie, Letitia and Anton decided to have dinner together at a nearby restaurant.  Julie orders $10 worth of food, Letitia orders $20 worth of food,
    and Anton orders $30 worth of food.  How much should each pay in tips if they want to split a 20% tip for the whole meal evenly?"""
    # Define the total cost of the meal
    total_cost = 10 + 20 + 30

    # Calculate the amount of the tip
    tip_amount = total_cost * 0.2

    # Calculate the total amount to be paid by each person
    individual_total = (total_cost + tip_amount) / 3

    # Calculate the amount of tip to be paid by each person
    individual_tip = tip_amount / 3

    # Display the amount of tip to be paid by each person
    result = individual_tip
    return result

print(solution())