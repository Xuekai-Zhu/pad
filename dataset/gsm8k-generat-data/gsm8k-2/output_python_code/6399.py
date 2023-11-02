def solution():
    """Dan spent $32 buying a new backpack, 1 pack of pens, 1 pack of pencils, and 5 multi-subject notebooks for school. If the backpack costs $15 and both the pens and pencils cost $1.00 each, how much did each notebook cost?"""
    total_cost = 32
    backpack_cost = 15
    pen_cost = 1
    pencil_cost = 1
    notebook_cost = (total_cost - backpack_cost - (pen_cost * 2) - (pencil_cost * 2)) / 5
    result = notebook_cost
    return result

print(solution())