def solution():
    total_points = 30+28+32+34+26  # Calculate the total points scored in the week
    games_played = 5  # The player played 5 games in the week
    average_points = total_points/games_played  # Calculate the average points per game

    if average_points >= 30: # If the average points are 30 or more...
        salary = 10000  # ...the player gets paid $10,000
    else: # If the average points are less than 30...
        salary = 8000  # ...the player gets paid $8,000

    result = salary
    return result

print(solution())