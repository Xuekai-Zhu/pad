def solution():
    """Jaron wants to raise enough money selling candy bars to win the Nintendo Switch prize. He needs 2000 points for the Nintendo Switch. He has already sold 8 chocolate bunnies that are worth 100 points each. Each Snickers bar he sells earns 25 points. How many Snickers bars does he need to sell the win the Nintendo Switch?"""
    # Define the number of points already earned and the target number of points
    earned_points = 8 * 100
    target_points = 2000

    # Calculate the number of Snickers bars needed to reach the target number of points
    snickers_needed = (target_points - earned_points) / 25

    # Round up to the nearest integer
    snickers_needed = math.ceil(snickers_needed)

    # return the result
    result = snickers_needed
    return result

print(solution())