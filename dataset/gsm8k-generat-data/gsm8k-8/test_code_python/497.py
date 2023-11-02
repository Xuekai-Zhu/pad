def solution():
    # Calculate the average points per game for the week
    total_points = 30 + 28 + 32 + 34 + 26
    average_points = total_points / 5

    # Determine the player's pay based on their average points per game
    if average_points >= 30:
        pay = 10000
    else:
        pay = 8000

    result = pay
    return result

print(solution())