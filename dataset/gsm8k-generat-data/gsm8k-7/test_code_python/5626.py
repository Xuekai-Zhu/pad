def solution():
    total_students = 2000
    num_voters = total_students * 0.25
    winner_percentage = 0.55

    # Calculate the number of votes the winner received
    winner_votes = num_voters * winner_percentage

    # Calculate the number of votes the loser received
    loser_votes = num_voters * (1 - winner_percentage)

    # Calculate the difference in votes between the winner and loser
    difference = winner_votes - loser_votes
    result = difference
    return result

print(solution())