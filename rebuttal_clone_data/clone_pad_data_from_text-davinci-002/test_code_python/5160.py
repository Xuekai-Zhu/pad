def solution():
    lily_ducks = 20
    lily_geese = 10
    rayden_ducks = lily_ducks * 3
    rayden_geese = lily_geese * 4
    total_animals = rayden_ducks + rayden_geese
    total_lily = lily_ducks + lily_geese
    difference = total_animals - total_lily
    result = difference
    
    return result

print(solution())