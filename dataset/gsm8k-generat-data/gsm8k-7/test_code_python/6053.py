def solution():
    total_points = 270
    num_players = 9
    num_players_with_known_score = 5
    avg_score_per_known_player = 50

    # Calculate the total points scored by the remaining players
    total_points_remaining_players = total_points - (num_players_with_known_score * avg_score_per_known_player)

    # Calculate the number of remaining players
    num_remaining_players = num_players - num_players_with_known_score

    # Calculate the average score per remaining player
    avg_score_remaining_players = total_points_remaining_players / num_remaining_players 
    result = round(avg_score_remaining_players)

    return result

print(solution())