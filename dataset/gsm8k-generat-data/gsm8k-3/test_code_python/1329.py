def solution():
    """3 people run for president. John manages to capture 150 votes. James captures 70% of the remaining vote. If there were 1150 people voting, how many more votes did the third guy get than John?"""
    # Calculate the number of votes remaining after John's capture
    remaining_votes = 1150 - 150

    # Calculate James' number of votes
    james_votes = remaining_votes * 0.7

    # Calculate the number of votes for the third guy
    third_guy_votes = remaining_votes - james_votes - 150

    # Calculate the difference between the third guy's votes and John's votes
    difference = third_guy_votes - 150

    # Display the difference in votes
    result = difference
    return result

print(solution())