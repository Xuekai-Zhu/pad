def solution():
    """In the last student council election, the winner got 55% of the votes and the loser got the rest. If the school has 2000 students, but only 25% of them voted, how many more votes did the winner get than the loser?"""
    total_students = 2000
    percent_voted = 25
    total_voted = total_students * (percent_voted / 100)
    winner_percent = 55
    loser_percent = 100 - winner_percent
    winner_votes = total_voted * (winner_percent / 100)
    loser_votes = total_voted * (loser_percent / 100)
    vote_difference = winner_votes - loser_votes
    result = vote_difference
    return result

print(solution())