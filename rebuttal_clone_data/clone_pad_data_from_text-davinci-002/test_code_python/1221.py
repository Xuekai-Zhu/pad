def solution():
    ducks_with_5_ducklings = 2
    ducks_with_3_ducklings = 6
    ducks_with_6_ducklings = 9
    total_ducks = ducks_with_5_ducklings + ducks_with_3_ducklings + ducks_with_6_ducklings
    total_ducklings = (ducks_with_5_ducklings * 5) + (ducks_with_3_ducklings * 3) + (ducks_with_6_ducklings * 6)
    result = (total_ducks, total_ducklings)
    
    return result

print(solution())