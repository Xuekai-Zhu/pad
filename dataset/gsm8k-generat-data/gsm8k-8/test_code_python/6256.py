def solution():
    # Define the variables
    average_score_per_round = 287
    total_rounds = 10
    total_players = 4
    current_score = 10440

    # Calculate the current average score per player
    current_average_score_per_player = current_score / (total_rounds * total_players)

    # Calculate the total points needed to tie the league record
    total_points_needed = average_score_per_round * total_rounds * total_players

    # Calculate the minimum average score per player needed to tie the league record
    minimum_average_score_per_player = (total_points_needed - current_score) / (total_players * (total_rounds - 1))

    # Calculate the difference between the minimum average score per player and the current league record
    points_less_than_record = average_score_per_round - minimum_average_score_per_player

    result = round(points_less_than_record, 2)
    return result

print(solution())