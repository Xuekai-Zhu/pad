def solution():
    """Dan spent $32 buying a new backpack, 1 pack of pens, 1 pack of pencils and 5 multi-subject notebooks for school.  If the backpack costs $15 and both the pens and pencils cost $1.00 each, how much did each notebook cost?"""
    # Define the cost of each item
    BACKPACK_COST = 15
    PEN_COST = 1
    PENCIL_COST = 1

    # Calculate the total cost of the pens and pencils
    writing_supplies_cost = PEN_COST + PENCIL_COST

    # Calculate the total cost of everything except the notebooks
    other_expenses = BACKPACK_COST + writing_supplies_cost

    # Calculate the cost per notebook
    notebook_cost = (32 - other_expenses) / 5

    # Display the cost per notebook
    result = notebook_cost
    return result

print(solution())