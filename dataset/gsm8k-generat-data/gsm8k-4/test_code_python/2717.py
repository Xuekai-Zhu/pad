def solution():
    """There are 322 voters in District 1. District 2 has 19 less voters than District 3. District 3 has twice as many voters as District 1. How many total voters are in Districts 1 - 3?"""
    # Define the number of voters in District 1
    district1_voters = 322

    # Calculate the number of voters in District 3
    district3_voters = district1_voters * 2

    # Calculate the number of voters in District 2
    district2_voters = district3_voters - 19

    # Calculate the total number of voters in Districts 1-3
    total_voters = district1_voters + district2_voters + district3_voters

    # return the result
    result = total_voters
    return result

print(solution())