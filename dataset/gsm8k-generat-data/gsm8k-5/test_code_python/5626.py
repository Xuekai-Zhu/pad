def solution():
    total_students = 2000  # The school has 2000 students
    voting_percentage = 0.25  # Only 25% of the students voted
    total_votes = total_students * voting_percentage  # Calculate the total number of votes cast
    winner_percentage = 0.55  # The winner got 55% of the votes
    loser_percentage = 1 - winner_percentage  # The loser got the rest of the votes

    # Calculate the number of votes for the winner and the loser
    winner_votes = total_votes * winner_percentage
    loser_votes = total_votes * loser_percentage

    # Calculate the difference in the number of votes between the winner and the loser
    difference = winner_votes - loser_votes
    result = difference
    return result

print(solution())