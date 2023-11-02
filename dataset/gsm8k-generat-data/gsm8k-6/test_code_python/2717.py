def solution():
    # Calculate the number of voters in each district
    voters_D1 = 322
    voters_D3 = 2 * voters_D1
    voters_D2 = voters_D3 - 19

    # Calculate the total number of voters in Districts 1-3
    total_voters = voters_D1 + voters_D2 + voters_D3
    result = total_voters
    return result

print(solution())