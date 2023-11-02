def solution():
    # Calculate the number of votes Mark got in the first area
    votes_first_area = 0.7 * 100000

    # Calculate the total number of voters in the remaining area
    remaining_voters = 100000 - votes_first_area / 0.7

    # Calculate the total number of votes Mark got in the remaining area
    votes_remaining_area = 2 * votes_first_area

    # Calculate the total number of votes Mark got
    total_votes = votes_first_area + votes_remaining_area

    result = total_votes
    return result

print(solution())