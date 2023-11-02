def solution():
    """There are 322 voters in District 1. District 2 has 19 less voters than District 3. District 3 has twice as many voters as District 1. How many total voters are in Districts 1 - 3?"""
    voters_d1 = 322
    voters_d3 = voters_d1 * 2
    voters_d2 = voters_d3 - 19
    total_voters = voters_d1 + voters_d2 + voters_d3
    result = total_voters
    return result

print(solution())