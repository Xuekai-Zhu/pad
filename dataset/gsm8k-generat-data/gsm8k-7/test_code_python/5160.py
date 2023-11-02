def solution():
    lily_ducks = 20
    lily_geese = 10

    rayden_ducks = 3 * lily_ducks
    rayden_geese = 4 * lily_geese

    ducks_diff = rayden_ducks - lily_ducks
    geese_diff = rayden_geese - lily_geese

    total_diff = ducks_diff + geese_diff
    result = total_diff
    return result

print(solution())