def solution():
    """3 people run for president. John manages to capture 150 votes. James captures 70% of the remaining vote. If there were 1150 people voting, how many more votes did the third guy get than John?"""
    total_votes = 1150
    john_votes = 150
    remaining_votes = total_votes - john_votes
    james_votes = 0.7 * remaining_votes
    third_guy_votes = total_votes - john_votes - james_votes
    difference = third_guy_votes - john_votes
    result = difference
    return result

print(solution())