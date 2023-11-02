def solution():
    # Calculate the number of students who voted
    num_voters = 2000 * 0.25

    # Calculate the number of votes for the winner
    winner_votes = 0.55 * num_voters

    # Calculate the number of votes for the loser
    loser_votes = num_voters - winner_votes

    # Calculate the difference between the winner's and loser's votes
    vote_difference = winner_votes - loser_votes
    result = vote_difference
    return result

print(solution())