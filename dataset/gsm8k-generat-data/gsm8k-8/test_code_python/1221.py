def solution():
    # Calculate the total number of ducks with 5 ducklings each
    ducks_with_5 = 2
    ducklings_with_5 = 5
    total_ducks_with_5 = ducks_with_5 * ducklings_with_5

    # Calculate the total number of ducks with 3 ducklings each
    ducks_with_3 = 6
    ducklings_with_3 = 3
    total_ducks_with_3 = ducks_with_3 * ducklings_with_3

    # Calculate the total number of ducks with 6 ducklings each
    ducks_with_6 = 9
    ducklings_with_6 = 6
    total_ducks_with_6 = ducks_with_6 * ducklings_with_6

    # Calculate the total number of ducks and ducklings
    total_ducks_and_ducklings = total_ducks_with_5 + total_ducks_with_3 + total_ducks_with_6
    result = total_ducks_and_ducklings
    return result

print(solution())