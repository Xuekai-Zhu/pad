def solution():
    """Rayden bought three times as many ducks as Lily from the market. He also bought four times as many geese as Lily. If Lily bought 20 ducks and 10 geese, how many more ducks and geese do Rayden have more than Lily altogether?"""
    lily_ducks = 20
    lily_geese = 10
    rayden_ducks = lily_ducks * 3
    rayden_geese = lily_geese * 4
    total_ducks = rayden_ducks - lily_ducks
    total_geese = rayden_geese - lily_geese
    result = total_ducks + total_geese
    return result

print(solution())