def solution():
    """Krishna and Callum are playing a game where they earn 10 points if they win any round. If they played eight matches and Krishna won 3/4 of the matches, what is the total number of points that Callum earned?"""
    total_matches = 8
    krishna_wins = total_matches * 3/4
    callum_wins = total_matches - krishna_wins
    callum_points = callum_wins * 10
    result = callum_points
    return result

print(solution())