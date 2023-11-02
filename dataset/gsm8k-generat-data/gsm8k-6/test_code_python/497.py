def solution():
    # Calculate the player's average points per game for the week
    total_points = 30 + 28 + 32 + 34 + 26
    average_points = total_points / 5

    # Calculate the player's weekly earnings based on the average points
    if average_points >= 30:
        weekly_earnings = 10000
    else:
        weekly_earnings = 8000
    result = weekly_earnings
    return result

print(solution())