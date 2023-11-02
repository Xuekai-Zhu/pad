def solution():
    """3 people run for president. John manages to capture 150 votes. James captures 70% of the remaining vote. If there were 1150 people voting, how many more votes did the third guy get than John?"""
    # Define the total number of voters and the number of votes captured by John
    total_voters = 1150
    john_votes = 150

    # Calculate the number of remaining votes after John's capture
    remaining_votes = total_voters - john_votes

    # Calculate the number of votes captured by James
    james_votes = remaining_votes * 0.7

    # Calculate the number of votes captured by the third candidate
    third_candidate_votes = remaining_votes - james_votes - john_votes

    # Calculate the difference between the number of votes captured by the third candidate and John
    difference = third_candidate_votes - john_votes

    # return the result
    result = difference
    return result

print(solution())