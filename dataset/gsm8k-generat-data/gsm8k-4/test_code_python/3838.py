def solution():
    """Kim orders a $10 meal and a drink for 2.5. She gives a 20% tip. She pays with a $20 bill. How much does she get in change?"""
    # Define the meal cost and the drink cost
    meal_cost = 10
    drink_cost = 2.5

    # Calculate the total cost of the meal and drink
    total_cost = meal_cost + drink_cost

    # Calculate the amount of the tip
    tip = total_cost * 0.2

    # Calculate the total amount to be paid
    total_paid = total_cost + tip

    # Calculate the amount of change
    change = 20 - total_paid

    # return the result
    result = change
    return result

print(solution())