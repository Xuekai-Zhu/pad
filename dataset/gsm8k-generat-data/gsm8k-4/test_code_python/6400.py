def solution():
    """Dan spent $32 buying a new backpack, 1 pack of pens, 1 pack of pencils and 5 multi-subject notebooks for school. If the backpack costs $15 and both the pens and pencils cost $1.00 each, how much did each notebook cost?"""
    # Define the cost of the backpack, pens, and pencils
    backpack_cost = 15
    pens_cost = 1
    pencils_cost = 1

    # Calculate the total cost of the pens and pencils
    pen_pencil_cost = (32 - backpack_cost) - 5

    # Calculate the cost per notebook
    notebook_cost = pen_pencil_cost / 5

    # return the result
    result = notebook_cost
    return result

print(solution())