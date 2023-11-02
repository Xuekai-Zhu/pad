def solution():
    """Marty and Biff were both running for student council president. A poll was taken to see how the candidate’s campaigns were going. 45% of the people polled said they were voting for Biff and 8% were undecided. The rest said they are voting for Marty. If 200 people were polled, how many said they are voting for Marty?"""
    biff_voters = 0.45 * 200
    undecided_voters = 0.08 * 200
    marty_voters = 200 - biff_voters - undecided_voters
    result = marty_voters
    return result

print(solution())