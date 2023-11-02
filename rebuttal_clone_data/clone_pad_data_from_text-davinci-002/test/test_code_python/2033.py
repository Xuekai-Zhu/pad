def solution():
    jeanine_pencils = 18
    clare_pencils = jeanine_pencils / 2
    given_away = jeanine_pencils / 3
    jeanine_left = jeanine_pencils - given_away
    result = jeanine_left - clare_pencils
    return result

print(solution())