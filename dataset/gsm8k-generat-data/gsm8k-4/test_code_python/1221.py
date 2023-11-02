def solution():
    """Mary sees a flock of ducks crossing the street. There are 2 ducks with 5 ducklings each, 6 ducks with 3 ducklings each, and 9 ducks with 6 ducklings each. How many ducks and ducklings are there total?"""
    # Calculate the total number of ducks and ducklings
    total_ducks = 2 + 6 + 9
    total_ducklings = (2 * 5) + (6 * 3) + (9 * 6)

    # return the result as a tuple
    result = (total_ducks, total_ducklings)
    return result

print(solution())