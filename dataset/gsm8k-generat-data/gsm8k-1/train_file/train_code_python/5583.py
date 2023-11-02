def solution():
    """Marty and Biff were both running for student council president. A poll was taken to see how the candidate’s campaigns were going. 45% of the people polled said they were voting for Biff and 8% were undecided. The rest said they are voting for Marty. If 200 people were polled, how many said they are voting for Marty?"""
    biff_percent = 45
    undecided_percent = 8
    marty_percent = 100 - (biff_percent + undecided_percent)
    total_polled = 200
    marty_votes = (marty_percent/100) * total_polled
    result = marty_votes
    return result

print(solution())