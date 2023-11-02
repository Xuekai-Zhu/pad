def solution():
    """Josh has 9 dollars. He spent $1.75 on a drink, and then spent another $1.25. How much money, in dollars, does Josh have left?"""
    # Define the initial amount Josh has
    initial_amount = 9

    # Calculate the amount Josh spent on the drink
    drink_cost = 1.75

    # Calculate the amount Josh spent on something else
    other_cost = 1.25

    # Calculate the total amount Josh spent
    total_cost = drink_cost + other_cost

    # Calculate the amount Josh has left
    amount_left = initial_amount - total_cost

    # Display the amount Josh has left
    result = amount_left
    return result

print(solution())