def solution():
    """Marcy's grade is electing their class president. Marcy got three times as many votes as Barry, who got twice as many as 3 more than the number of votes Joey got. If Joey got 8 votes, how many votes did Marcy get?"""
    joey_votes = 8
    barry_votes = 2 * (joey_votes + 3)
    marcy_votes = 3 * barry_votes
    result = marcy_votes
    return result

print(solution())