def solution():
    hits_in_first_20_games = 2 * 20
    total_games = 20 + 10
    desired_average = 3
    current_average = hits_in_first_20_games / 20
    additional_hits_needed = (total_games * desired_average) - hits_in_first_20_games
    additional_games_needed = additional_hits_needed / desired_average
    result = additional_games_needed
    return result

print(solution())