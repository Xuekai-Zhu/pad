def solution():
    
    total_votes = 80
    winner_votes = total_votes * (3/4)
    loser_votes = total_votes - winner_votes
    result = loser_votes
    return result

print(solution())