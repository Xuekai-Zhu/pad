def solution():
    voters_d1 = 322
    voters_d3 = voters_d1 * 2
    voters_d2 = voters_d3 - 19

    # Calculate the total number of voters in all three districts
    total_voters = voters_d1 + voters_d2 + voters_d3
    result = total_voters
    return result

print(solution())