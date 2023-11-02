def solution():
    cost_per_yard = 7.50  # The cost of both fabrics per yard is $7.50
    cost_checkered = 75  # Vivi spent $75 on checkered fabric
    cost_plain = 45  # Vivi spent $45 on plain fabric

    # Calculate the total yards of checkered fabric
    yards_checkered = cost_checkered / cost_per_yard

    # Calculate the total yards of plain fabric
    yards_plain = cost_plain / cost_per_yard

    # Calculate the total yards of fabric Vivi bought
    total_yards = yards_checkered + yards_plain
    result = total_yards
    return result

print(solution())