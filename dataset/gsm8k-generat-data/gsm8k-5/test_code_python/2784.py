def solution():
    notebook_cost = 4.00  # Each notebook costs 4 dollars
    pen_cost = 1.50  # Each pen costs 1.50 dollars
    num_notebooks = 2  # Rubble needs to buy 2 notebooks
    num_pens = 2  # Rubble needs to buy 2 pens
    total_cost = (notebook_cost * num_notebooks) + (pen_cost * num_pens)  # Calculate the total cost
    change = 15 - total_cost  # Calculate the change
    result = change
    return result

print(solution())