def solution():
    # Define the number of points Jaron already earned
    points_already_earned = 8 * 100

    # Define the number of points needed to win the prize
    points_needed = 2000 - points_already_earned

    # Calculate the number of Snickers bars Jaron needs to sell
    snickers_bars_needed = points_needed / 25
    result = snickers_bars_needed
    return result

print(solution())