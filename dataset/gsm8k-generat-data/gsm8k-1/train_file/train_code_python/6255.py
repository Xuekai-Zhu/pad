def solution():
    """George's bowling team is one round away from breaking the league record for most points scored in a season. The old record is an average score per player of 287 per round. Each team has 4 players and there are 10 rounds in the season. Through the first 9 rounds, his team has scored a total of 10,440. How many points less than the current league record per game average is the minimum average they need to score, per player, in the final round to tie the league record?"""
    current_record = 287 * 4
    total_points_so_far = 10440
    total_players = 4
    total_rounds = 10
    rounds_played_so_far = 9
    points_needed_to_tie_record = current_record * total_rounds - total_points_so_far
    points_needed_per_player = points_needed_to_tie_record / total_players / (total_rounds - rounds_played_so_far)
    points_less_than_record = current_record - points_needed_per_player
    result = points_less_than_record
    return result

print(solution())