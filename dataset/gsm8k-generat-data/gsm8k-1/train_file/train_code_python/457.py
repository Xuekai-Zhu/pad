def solution():
    """Marcy's grade is electing their class president. Marcy got three times as many votes as Barry, who got twice as many as 3 more than the number of votes Joey got. If Joey got 8 votes, how many votes did Marcy get?"""
    joey_votes = 8
    barry_votes = (joey_votes + 3) * 2
    marcy_votes = barry_votes * 3
    result = marcy_votes
    return result

print(solution())