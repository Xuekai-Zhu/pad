def solution():
    total_voters = 100000
    percentage_of_votes_won = 0.7

    # Calculate the number of votes won in the area with 100,000 voters
    votes_won_in_area = total_voters * percentage_of_votes_won

    # Calculate the total number of voters in the remaining area
    remaining_voters = total_voters - total_voters * percentage_of_votes_won

    # Calculate the total number of votes Mark got in the remaining area
    total_votes_in_remaining_area = votes_won_in_area * 2
    total_votes = votes_won_in_area + total_votes_in_remaining_area
    result = total_votes
    return result

print(solution())