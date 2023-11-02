def solution():
    """Dan spent $32 buying a new backpack, 1 pack of pens, 1 pack of pencils and 5 multi-subject notebooks for school. If the backpack costs $15 and both the pens and pencils cost $1.00 each, how much did each notebook cost?"""
    total_cost = 32
    backpack_cost = 15
    pens_and_pencils_cost = 2
    notebook_quantity = 5
    notebook_cost = (total_cost - backpack_cost - pens_and_pencils_cost) / notebook_quantity
    result = notebook_cost
    return result

print(solution())