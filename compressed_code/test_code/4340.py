def solution():
    
    total_students = 2000
    voting_percentage = 0.25
    total_votes = total_students * voting_percentage
    winner_percentage = 0.55
    winner_votes = winner_percentage * total_votes
    loser_votes = total_votes - winner_votes
    difference_votes = winner_votes - loser_votes
    result = difference_votes
    return result

print(solution())