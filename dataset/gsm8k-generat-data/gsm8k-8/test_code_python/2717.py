def solution():
    # Define the number of voters in District 1
    dist1_voters = 322

    # Calculate the number of voters in District 3
    dist3_voters = 2 * dist1_voters

    # Calculate the number of voters in District 2
    dist2_voters = dist3_voters - 19

    # Calculate the total number of voters in all 3 districts
    total_voters = dist1_voters + dist2_voters + dist3_voters
    result = total_voters
    return result

print(solution())