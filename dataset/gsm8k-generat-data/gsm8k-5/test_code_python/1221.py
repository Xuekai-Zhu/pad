def solution():
    # Number of ducks with 5 ducklings each
    ducks_5 = 2
    ducklings_5 = 5
    # Number of ducks with 3 ducklings each
    ducks_3 = 6
    ducklings_3 = 3
    # Number of ducks with 6 ducklings each
    ducks_6 = 9
    ducklings_6 = 6
    
    # Calculate the total number of ducks and ducklings
    total_ducks = ducks_5 + ducks_3 + ducks_6
    total_ducklings = (ducks_5 * ducklings_5) + (ducks_3 * ducklings_3) + (ducks_6 * ducklings_6)
    
    result = "There are {} ducks and {} ducklings total.".format(total_ducks, total_ducklings)
    return result

print(solution())