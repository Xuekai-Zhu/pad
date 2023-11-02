def solution():
    jeanine_pencils = 18
    clare_pencils = jeanine_pencils / 2
    abby_pencils = jeanine_pencils / 3

    # Calculate the number of pencils that Jeanine has left after giving some to Abby
    jeanine_pencils_left = jeanine_pencils - abby_pencils

    # Calculate the difference between the number of pencils Jeanine has left and the number Clare has
    difference = jeanine_pencils_left - clare_pencils
    result = difference
    return result

print(solution())