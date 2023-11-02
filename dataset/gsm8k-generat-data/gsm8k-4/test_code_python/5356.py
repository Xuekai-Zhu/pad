def solution():
    """Vivi bought fabric to make new pillows for her bed. She spent $75 on checkered fabric and $45 on plain fabric. If both fabrics cost $7.50 per yard, how many total yards of fabric did she buy?"""
    # Define the cost and price per yard of each type of fabric
    CHECKERED_COST = 75
    PLAIN_COST = 45
    PRICE_PER_YARD = 7.5

    # Calculate the number of yards of checkered fabric
    checkered_yards = CHECKERED_COST / PRICE_PER_YARD

    # Calculate the number of yards of plain fabric
    plain_yards = PLAIN_COST / PRICE_PER_YARD

    # Calculate the total yards of fabric bought
    total_yards = checkered_yards + plain_yards

    # return the result
    result = total_yards
    return result

print(solution())