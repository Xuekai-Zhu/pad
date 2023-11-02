def solution():
    """Krishna and Callum are playing a game where they earn 10 points if they win any round. If they played eight matches and Krishna won 3/4 of the matches, what is the total number of points that Callum earned?"""
    rounds_played = 8
    krishna_won = 3/4 * rounds_played
    callum_won = rounds_played - krishna_won
    points_per_round = 10
    callum_points = callum_won * points_per_round
    result = callum_points
    return result

print(solution())