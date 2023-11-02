def solution():
    voters_district1 = 322  # given that District 1 has 322 voters
    voters_district3 = voters_district1 * 2  # District 3 has twice as many voters as District 1
    voters_district2 = voters_district3 - 19  # District 2 has 19 less voters than District 3
    
    # Calculate total voters in Districts 1-3
    total_voters = voters_district1 + voters_district2 + voters_district3
    result = total_voters
    return result

print(solution())