def solution():
    num_players = 4
    num_rounds = 10
    old_record_avg = 287
    total_old_record = num_players * num_rounds * old_record_avg
    current_score = 10440

    # Calculate the minimum total score needed to tie the league record
    min_total_score = total_old_record + old_record_avg

    # Calculate the minimum per player average needed to tie the league record
    min_avg = min_total_score / (num_players * num_rounds)

    # Calculate the points less than the current league record per game average
    points_less = old_record_avg - min_avg

    result = points_less
    return result

print(solution())