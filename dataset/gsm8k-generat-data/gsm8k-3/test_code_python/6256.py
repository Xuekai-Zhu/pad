def solution():
    """George's bowling team is one round away from breaking the league record for most points scored in a season. The old record is an average score per player of 287 per round. Each team has 4 players and there are 10 rounds in the season. Through the first 9 rounds, his team has scored a total of 10,440. How many points less than the current league record per game average is the minimum average they need to score, per player, in the final round to tie the league record?"""
    # Define the current league record for average score per player per round
    RECORD_AVERAGE = 287

    # Define the number of players in a team and the number of rounds in a season
    PLAYERS_PER_TEAM = 4
    ROUNDS_PER_SEASON = 10

    # Calculate the total points needed to break the record
    total_points_needed = RECORD_AVERAGE * PLAYERS_PER_TEAM * ROUNDS_PER_SEASON

    # Calculate the total points scored in the first 9 rounds
    total_points_scored = 10440

    # Calculate the total points needed in the final round to tie the record
    points_needed_in_final_round = total_points_needed - total_points_scored

    # Calculate the minimum average score per player in the final round to tie the record
    min_average_score_per_player = points_needed_in_final_round / PLAYERS_PER_TEAM

    # Calculate the difference between the minimum average and the current record
    difference = RECORD_AVERAGE - min_average_score_per_player

    # Display the difference
    result = difference
    return result

print(solution())