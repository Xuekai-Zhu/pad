def solution():
    total_votes = 1150  # Total number of votes cast
    john_votes = 150  # Number of votes John received
    remaining_votes = total_votes - john_votes  # Number of votes remaining for other candidates
    james_votes = 0.7 * remaining_votes  # Number of votes James received
    third_guy_votes = remaining_votes - james_votes  # Number of votes the third guy received

    # Calculate the difference between the third guy's votes and John's votes
    difference = third_guy_votes - john_votes
    result = difference
    return result

print(solution())