def solution():
    # Calculate the total points needed to break the league record
    total_points_needed = 287 * 4 * 10  # average score per player of 287 per round, 4 players, and 10 rounds

    # Calculate the minimum average per player needed to tie the record
    min_avg_needed = (total_points_needed - 10440) / 4  # subtract the total score through first 9 rounds from total points needed and divide by 4 players

    # Calculate the difference between the current league record per game average and the minimum average needed to tie the record
    difference = 287 - min_avg_needed
    result = difference
    return result

print(solution())