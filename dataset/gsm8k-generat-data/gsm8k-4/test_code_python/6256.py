def solution():
    """George's bowling team is one round away from breaking the league record for most points scored in a season. The old record is an average score per player of 287 per round. Each team has 4 players and there are 10 rounds in the season. Through the first 9 rounds, his team has scored a total of 10,440. How many points less than the current league record per game average is the minimum average they need to score, per player, in the final round to tie the league record?"""
    # Define the current record and the number of players and rounds
    current_record = 287
    num_players = 4
    num_rounds = 10

    # Calculate the current total score of George's team
    current_score = 10440

    # Calculate the minimum total score needed to tie the record
    min_total_score = current_record * num_players * num_rounds

    # Calculate the minimum score per player needed in the final round
    min_score_per_player = (min_total_score - current_score) / (num_players * (num_rounds-1))

    # Calculate the difference between the minimum score and the current record
    diff = current_record - min_score_per_player

    # Return the result
    result = diff
    return result

print(solution())