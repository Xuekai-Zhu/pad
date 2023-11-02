def solution():
    """Julie, Letitia and Anton decided to have dinner together at a nearby restaurant. Julie orders $10 worth of food, Letitia orders $20 worth of food, and Anton orders $30 worth of food. How much should each pay in tips if they want to split a 20% tip for the whole meal evenly?"""
    # Define the total cost of the meal
    total_cost = 10 + 20 + 30

    # Calculate the 20% tip
    tip = total_cost * 0.2

    # Calculate the total cost of the meal with the tip included
    total_cost_with_tip = total_cost + tip

    # Divide the total cost with tip by 3 to get the cost per person
    cost_per_person = total_cost_with_tip / 3

    # Calculate the amount of tip each person should pay
    tip_per_person = tip / 3

    result = tip_per_person
    return result

print(solution())