def solution():
    """Vivi bought fabric to make new pillows for her bed. She spent $75 on checkered fabric and $45 on plain fabric. If both fabrics cost $7.50 per yard, how many total yards of fabric did she buy?"""
    checkered_cost = 75
    plain_cost = 45
    fabric_cost_per_yard = 7.5
    total_cost = checkered_cost + plain_cost
    total_yards = total_cost / fabric_cost_per_yard
    result = total_yards
    return result

print(solution())