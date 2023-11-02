def solution():
    """Vivi bought fabric to make new pillows for her bed. She spent $75 on checkered fabric and $45 on plain fabric. If both fabrics cost $7.50 per yard, how many total yards of fabric did she buy?"""
    checkered_cost = 75
    plain_cost = 45
    cost_per_yard = 7.5
    total_checkered_yards = checkered_cost / cost_per_yard
    total_plain_yards = plain_cost / cost_per_yard
    total_yards = total_checkered_yards + total_plain_yards
    result = total_yards
    return result

print(solution())