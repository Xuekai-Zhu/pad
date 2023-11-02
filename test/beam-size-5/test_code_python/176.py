def solution():
    
    # Define the total number of students who voted
    total_students = 80

    # Calculate the number of votes the winner got
    winner_votes = total_students * 3/4

    # Calculate the number of votes the loser got
    loser_votes = total_students - winner_votes

    # Display the number of votes the loser got
    result = loser_votes
    return result

print(solution())