def solution():
    """Kim orders a $10 meal and a drink for 2.5.  She gives a 20% tip.  She pays with a $20 bill.  How much does she get in change?"""
    # Define the cost of the meal and drink
    meal_cost = 10
    drink_cost = 2.5

    # Calculate the total cost of the meal and drink
    total_cost = meal_cost + drink_cost

    # Calculate the 20% tip
    tip = total_cost * 0.2

    # Calculate the total amount to be paid, including the tip
    total_amount = total_cost + tip

    # Calculate the amount of change to be given
    change = 20 - total_amount

    # Display the amount of change
    result = change
    return result

print(solution())