def solution():
    total_voters = 100000  # There are 100,000 voters in the area
    votes_received = total_voters * 0.7  # Mark wins 70% of the votes in the area
    remaining_voters = total_voters - votes_received  # Calculate the number of voters in the remaining area
    remaining_votes = votes_received * 2  # Mark gets twice as many votes in the remaining area

    # Calculate the total number of votes Mark received
    total_votes = votes_received + remaining_votes
    result = total_votes
    return result

print(solution())