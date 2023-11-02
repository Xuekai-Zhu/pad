def solution():
    """3 people run for president. John manages to capture 150 votes. James captures 70% of the remaining vote. If there were 1150 people voting, how many more votes did the third guy get than John?"""
    total_voters = 1150
    john_votes = 150
    remaining_votes = total_voters - john_votes
    james_votes = remaining_votes * 0.7
    third_guy_votes = remaining_votes - james_votes - john_votes
    difference = third_guy_votes - john_votes
    result = difference
    return result

print(solution())