def solution():
    money_in_pocket = 15
    num_notebooks = 2
    notebook_price = 4.0
    num_pens = 2
    pen_price = 1.5

    # Calculate the total cost of all notebooks
    total_notebook_cost = num_notebooks * notebook_price

    # Calculate the total cost of all pens
    total_pen_cost = num_pens * pen_price

    # Calculate the total cost of all items
    total_cost = total_notebook_cost + total_pen_cost

    # Calculate the amount of money left in Rubble's pocket after the purchase
    money_left = money_in_pocket - total_cost
    result = money_left
    return result

print(solution())