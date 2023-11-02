def solution():
    """There are 322 voters in District 1. District 2 has 19 less voters than District 3. District 3 has twice as many voters as District 1. How many total voters are in Districts 1 - 3?"""
    # Define the number of voters in District 1
    voters_1 = 322

    # Calculate the number of voters in District 3
    voters_3 = voters_1 * 2

    # Calculate the number of voters in District 2
    voters_2 = voters_3 - 19

    # Calculate the total number of voters in all districts
    total_voters = voters_1 + voters_2 + voters_3

    # Display the total number of voters
    result = total_voters
    return result

print(solution())