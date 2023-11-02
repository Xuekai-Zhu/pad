def solution():
    """Jude bought three chairs for his house, all at the same price. He also bought a table that costs $50 and two sets of plates at $20 for each set. After giving the cashier $130, Jude got a $4 change. How much did each of the chairs cost?"""
    total_cost = 130 - 4
    chair_quantity = 3
    table_cost = 50
    plate_cost = 20*2
    chair_cost = (total_cost - table_cost - plate_cost) / chair_quantity
    result = chair_cost
    return result

print(solution())