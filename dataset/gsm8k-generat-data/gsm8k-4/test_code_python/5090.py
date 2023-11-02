def solution():
    """Mark is running for an election and wins 70% of the votes in an area with 100,000 voters. He got twice as many total votes in the remaining area. How many votes did he get in total?"""
    # Define the total number of voters and the percentage of votes won in the first area
    total_voters = 100000
    votes_percentage = 0.7

    # Calculate the number of votes won in the first area
    votes_won = total_voters * votes_percentage

    # Calculate the total number of votes in the remaining area
    remaining_votes = votes_won * 2

    # Calculate the total number of votes won
    total_votes = votes_won + remaining_votes

    # Return the result
    result = total_votes
    return result

print(solution())