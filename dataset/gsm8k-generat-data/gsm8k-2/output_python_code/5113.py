def solution():
    """Jaron wants to raise enough money selling candy bars to win the Nintendo Switch prize. He needs 2000 points for the Nintendo Switch. He has already sold 8 chocolate bunnies that are worth 100 points each. Each Snickers bar he sells earns 25 points. How many Snickers bars does he need to sell to win the Nintendo Switch?"""
    switch_points = 2000
    bunny_points = 8 * 100
    total_points = bunny_points

    snickers_points = 25
    snickers_needed = (switch_points - total_points) // snickers_points

    result = snickers_needed
    return result

print(solution())