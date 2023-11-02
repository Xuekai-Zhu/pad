def solution():
    # Calculate the number of dresses with pockets
    dresses_with_pockets = 24 / 2  # Half of the dresses have pockets

    # Calculate the number of dresses with 2 pockets
    dresses_with_2_pockets = dresses_with_pockets / 3

    # Calculate the number of dresses with 3 pockets
    dresses_with_3_pockets = dresses_with_pockets - dresses_with_2_pockets

    # Calculate the total number of pockets
    total_pockets = (dresses_with_2_pockets * 2) + (dresses_with_3_pockets * 3)

    result = total_pockets
    return result

print(solution())