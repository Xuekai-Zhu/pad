def solution():
    ducks = 25
    geese = ducks * 2 - 10
    new_ducks = 4
    ducks = ducks + new_ducks
    leaving_geese = 15 - 5
    geese = geese - leaving_geese
    result = geese - ducks
    return result

print(solution())