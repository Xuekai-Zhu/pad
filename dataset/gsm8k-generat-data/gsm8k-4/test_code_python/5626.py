def solution():
    """In the last student council election, the winner got 55% of the votes and the loser got the rest. If the school has 2000 students, but only 25% of them voted, how many more votes did the winner get than the loser?"""
    # Define the total number of students and the percentage that voted
    total_students = 2000
    vote_percentage = 0.25

    # Calculate the number of students that voted
    num_voters = total_students * vote_percentage

    # Calculate the number of votes received by the winner
    winner_votes = num_voters * 0.55

    # Calculate the number of votes received by the loser
    loser_votes = num_voters - winner_votes

    # Calculate the difference in votes between the winner and loser
    vote_difference = winner_votes - loser_votes

    # Return the result
    result = vote_difference
    return result

print(solution())