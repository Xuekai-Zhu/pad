def solution():
    """Mary sees a flock of ducks crossing the street. There are 2 ducks with 5 ducklings each, 6 ducks with 3 ducklings each, and 9 ducks with 6 ducklings each. How many ducks and ducklings are there total?"""
    duck_1 = 2
    duck_1_ducklings = 5
    duck_2 = 6
    duck_2_ducklings = 3
    duck_3 = 9
    duck_3_ducklings = 6
    total_ducks = duck_1 + duck_2 + duck_3
    total_ducklings = (duck_1 * duck_1_ducklings) + (duck_2 * duck_2_ducklings) + (duck_3 * duck_3_ducklings)
    result = f"{total_ducks} ducks and {total_ducklings} ducklings"
    return result

print(solution())