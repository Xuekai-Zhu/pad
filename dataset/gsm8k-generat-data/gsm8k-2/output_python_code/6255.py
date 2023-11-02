def solution():
    """George's bowling team is one round away from breaking the league record for most points scored in a season. The old record is an average score per player of 287 per round. Each team has 4 players and there are 10 rounds in the season. Through the first 9 rounds, his team has scored a total of 10,440. How many points less than the current league record per game average is the minimum average they need to score, per player, in the final round to tie the league record?"""
    record_per_round = 287 * 4
    total_record = record_per_round * 10
    current_average = 10440 / (9 * 4)
    minimum_average = (record_per_round - 10440) / 4
    points_less = record_per_round - minimum_average - current_average
    result = points_less
    return result

print(solution())