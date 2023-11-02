def solution():
    """Vivi bought fabric to make new pillows for her bed. She spent $75 on checkered fabric and $45 on plain fabric. If both fabrics cost $7.50 per yard, how many total yards of fabric did she buy?"""
    # Define the cost per yard of fabric
    FABRIC_COST = 7.5

    # Calculate the total yards of checkered fabric bought
    checkered_yards = 75 / FABRIC_COST

    # Calculate the total yards of plain fabric bought
    plain_yards = 45 / FABRIC_COST

    # Calculate the total yards of fabric bought
    total_yards = checkered_yards + plain_yards

    # Display the total yards of fabric bought
    result = total_yards
    return result

print(solution())