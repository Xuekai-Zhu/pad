def solution():
    points_needed = 2000  # Jaron needs 2000 points to win the Nintendo Switch
    points_earned = 8*100  # Jaron has already earned 800 points by selling 8 chocolate bunnies
    points_to_earn = points_needed - points_earned  # Jaron still needs to earn this many points
    snickers_points = 25  # Each Snickers bar earns 25 points

    # Calculate the number of Snickers bars Jaron needs to sell to earn the remaining points
    snickers_bars_needed = points_to_earn / snickers_points
    result = snickers_bars_needed
    return result

print(solution())