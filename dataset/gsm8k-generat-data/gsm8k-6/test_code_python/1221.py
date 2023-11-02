def solution():
    # Calculate the total number of ducklings
    total_ducklings = 2 * 5 + 6 * 3 + 9 * 6  # 2 ducks with 5 ducklings each, 6 ducks with 3 ducklings each, 9 ducks with 6 ducklings each
    # Calculate the total number of ducks (including those with ducklings)
    total_ducks = 2 + 6 + 9  # 2 ducks with ducklings, 6 ducks with ducklings, 9 ducks with ducklings
    # Add the number of ducklings to the number of ducks to get total
    total = total_ducklings + total_ducks 
    result = total
    return result

print(solution())