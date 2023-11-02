def solution():
    """Rayden bought three times as many ducks as Lily from the market. He also bought four times as many geese as Lily. If Lily bought 20 ducks and 10 geese, how many more ducks and geese do Rayden have more than Lily altogether?"""
    lily_ducks = 20
    rayden_ducks = 3 * lily_ducks
    lily_geese = 10
    rayden_geese = 4 * lily_geese
    total_ducks_more = rayden_ducks - lily_ducks
    total_geese_more = rayden_geese - lily_geese
    result = (total_ducks_more, total_geese_more)
    return result

print(solution())