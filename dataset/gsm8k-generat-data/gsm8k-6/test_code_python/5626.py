def solution():
    # Calculate the number of students who voted
    num_voters = 2000 * 0.25  

    # Calculate the number of votes received by the winner and loser
    winner_votes = num_voters * 0.55  
    loser_votes = num_voters - winner_votes  

    # Calculate the difference in number of votes between the winner and loser
    vote_diff = winner_votes - loser_votes
    result = vote_diff
    return result

print(solution())