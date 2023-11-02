def solution():
    """There are 322 voters in District 1. District 2 has 19 less voters than District 3. District 3 has twice as many voters as District 1. How many total voters are in Districts 1 - 3?"""
    district_1 = 322
    district_3 = district_1 * 2
    district_2 = district_3 - 19
    total_voters = district_1 + district_2 + district_3
    result = total_voters
    return result

print(solution())