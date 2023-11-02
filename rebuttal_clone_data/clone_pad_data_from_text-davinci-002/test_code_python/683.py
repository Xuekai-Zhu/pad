def solution():
    julia_has = 40
    game_cost = julia_has / 2
    julia_has -= game_cost
    in_game_cost = julia_has / 4
    julia_has -= in_game_cost
    result = julia_has
    return result

print(solution())