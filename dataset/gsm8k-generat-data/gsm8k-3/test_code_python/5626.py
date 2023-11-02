def solution():
    """In the last student council election, the winner got 55% of the votes and the loser got the rest. If the school has 2000 students, but only 25% of them voted, how many more votes did the winner get than the loser?"""
    # Define the number of students in the school and the percentage of students who voted
    total_students = 2000
    vote_percentage = 0.25

    # Calculate the number of students who voted
    num_voters = total_students * vote_percentage

    # Calculate the number of votes the winner and loser received
    winner_votes = num_voters * 0.55
    loser_votes = num_voters * 0.45

    # Calculate the difference in votes between the winner and loser
    vote_difference = winner_votes - loser_votes

    # Display the vote difference
    result = vote_difference
    return result

print(solution())