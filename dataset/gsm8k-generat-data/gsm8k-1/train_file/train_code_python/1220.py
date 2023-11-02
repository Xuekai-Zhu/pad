def solution():
    """Mary sees a flock of ducks crossing the street. There are 2 ducks with 5 ducklings each, 6 ducks with 3 ducklings each, and 9 ducks with 6 ducklings each. How many ducks and ducklings are there total?"""
    ducks_with_5 = 2
    ducklings_in_5 = 5
    ducks_with_3 = 6
    ducklings_in_3 = 3
    ducks_with_6 = 9
    ducklings_in_6 = 6
    total_ducks = ducks_with_5 + ducks_with_3 + ducks_with_6
    total_ducklings = (ducks_with_5 * ducklings_in_5) + (ducks_with_3 * ducklings_in_3) + (ducks_with_6 * ducklings_in_6)
    result = {"total_ducks": total_ducks, "total_ducklings": total_ducklings}
    return result

print(solution())