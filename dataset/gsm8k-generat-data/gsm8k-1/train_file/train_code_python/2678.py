def solution():
    """Gretchen bowled a 120. Mitzi bowled a 113. Beth bowled an 85. What was their average bowling score?"""
    gretchen_score = 120
    mitzi_score = 113
    beth_score = 85
    total_score = gretchen_score + mitzi_score + beth_score
    num_players = 3
    avg_score = total_score / num_players
    result = avg_score
    return result

print(solution())