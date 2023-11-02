def solution():
    # Lisa visited 6 rehab centers
    lisa_rehabs = 6

    # Jude visited half the number of rehabs that Lisa did
    jude_rehabs = lisa_rehabs / 2

    # Han visited 2 less than twice the number of rehabs that Jude did
    han_rehabs = 2*jude_rehabs - 2

    # Jane visited 6 more than twice the number of rehabs that Han did
    jane_rehabs = 2*han_rehabs + 6

    # Calculate the total number of rehab centers visited
    total_rehabs = lisa_rehabs + jude_rehabs + han_rehabs + jane_rehabs

    # Return the result
    return total_rehabs

print(solution())