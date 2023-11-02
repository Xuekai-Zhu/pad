def solution():
    """Jaron wants to raise enough money selling candy bars to win the Nintendo Switch prize. He needs 2000 points for the Nintendo Switch. He has already sold 8 chocolate bunnies that are worth 100 points each. Each Snickers bar he sells earns 25 points. How many Snickers bars does he need to sell the win the Nintendo Switch?"""
    # Calculate the total points earned from the chocolate bunnies
    bunny_points = 8 * 100

    # Calculate the points still needed to earn the Nintendo Switch
    points_needed = 2000 - bunny_points

    # Calculate the number of Snickers bars needed to earn the remaining points
    snickers_needed = points_needed / 25

    # Round up to the nearest whole number
    snickers_needed = math.ceil(snickers_needed)

    # Display the number of Snickers bars needed
    result = snickers_needed
    return result

print(solution())