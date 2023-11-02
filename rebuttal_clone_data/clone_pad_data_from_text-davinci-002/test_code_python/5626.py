def solution():
    total_students = 2000
    percent_voted = 25
    total_votes = total_students * (percent_voted / 100)
    percent_winner = 55
    winner_votes = total_votes * (percent_winner / 100)
    loser_votes = total_votes - winner_votes
    votes_won_by = winner_votes - loser_votes
    result = votes_won_by
    return result

print(solution())