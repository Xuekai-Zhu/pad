def solution():
    
    lily_ducks = 20
    lily_geese = 10
    rayden_ducks = lily_ducks * 3
    rayden_geese = lily_geese * 4
    total_ducks = rayden_ducks - lily_ducks
    total_geese = rayden_geese - lily_geese
    result = total_ducks + total_geese
    return result

print(solution())