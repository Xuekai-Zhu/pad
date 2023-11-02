def solution():
    # Define the number of games and practice hours per game
    num_games = 8
    practice_hours_per_game = 4
    game_hours = 2

    # Calculate the total practice hours for both teams
    total_practice_hours = num_games * 2 * practice_hours_per_game

    # Calculate the total game hours for both teams
    total_game_hours = num_games * 2 * game_hours

    # Calculate the total hours Jerry spends at the field
    total_hours = total_practice_hours + total_game_hours
    result = total_hours
    return result

print(solution())