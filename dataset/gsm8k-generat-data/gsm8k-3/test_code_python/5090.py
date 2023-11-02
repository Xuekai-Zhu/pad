def solution():
    """Mark is running for an election and wins 70% of the votes in an area with 100,000 voters.  He got twice as many total votes in the remaining area.  How many votes did he get in total?"""
    # Calculate the number of votes Mark won in the first area
    votes_area1 = 0.7 * 100000

    # Calculate the total number of votes in the second area
    total_votes_area2 = 2.0 * votes_area1

    # Calculate the number of votes Mark won in the second area
    votes_area2 = total_votes_area2 - votes_area1

    # Calculate the total number of votes Mark got
    total_votes = votes_area1 + votes_area2

    # Display the total number of votes Mark got
    result = total_votes
    return result

print(solution())