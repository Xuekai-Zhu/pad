def solution():
    """Jaron wants to raise enough money selling candy bars to win the Nintendo Switch prize. He needs 2000 points for the Nintendo Switch. He has already sold 8 chocolate bunnies that are worth 100 points each. Each Snickers bar he sells earns 25 points. How many Snickers bars does he need to sell to win the Nintendo Switch?"""
    points_needed = 2000
    points_from_bunnies = 8 * 100
    points_from_snickers = points_needed - points_from_bunnies
    snickers_per_point = 1/25
    snickers_needed = points_from_snickers * snickers_per_point
    result = snickers_needed
    return result

print(solution())