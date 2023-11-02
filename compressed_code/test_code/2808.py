def solution():
    
    jeanine_pencils = 18
    clare_pencils = jeanine_pencils / 2
    abby_pencils = jeanine_pencils / 3
    jeanine_pencils -= abby_pencils
    difference = jeanine_pencils - clare_pencils
    result = difference
    return result

print(solution())