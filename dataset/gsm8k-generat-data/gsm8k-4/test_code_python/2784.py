def solution():
    """Rubble has $15 in his pocket and he needs to buy 2 notebooks and 2 pens. Each notebook cost $4.00 meanwhile each pen cost $1.50. How much money will be left from Rubble after the purchase?"""
    # Define the initial amount of money
    initial_money = 15

    # Define the cost of each notebook and pen
    notebook_cost = 4
    pen_cost = 1.5

    # Define the number of notebooks and pens needed
    notebooks_needed = 2
    pens_needed = 2

    # Calculate the total cost of the notebooks and pens
    notebook_total_cost = notebook_cost * notebooks_needed
    pen_total_cost = pen_cost * pens_needed
    total_cost = notebook_total_cost + pen_total_cost

    # Calculate the amount of money left after the purchase
    money_left = initial_money - total_cost

    # Return the result
    result = money_left
    return result

print(solution())