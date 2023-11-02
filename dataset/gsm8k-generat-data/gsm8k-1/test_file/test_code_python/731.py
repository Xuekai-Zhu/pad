def solution():
    """In a student council election, candidate A got 20% of the votes while candidate B got 50% more than candidate A's votes. The rest of the votes was given to candidate C. If there were 100 voters, how many votes did candidate C get?"""
    total_voters = 100
    a_percentage = 20
    b_percentage = a_percentage + (a_percentage * 0.5)
    c_percentage = 100 - (a_percentage + b_percentage)
    c_votes = (c_percentage / 100) * total_voters
    result = c_votes
    return result

print(solution())