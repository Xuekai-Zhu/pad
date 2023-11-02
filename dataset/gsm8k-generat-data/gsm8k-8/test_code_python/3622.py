def solution():
    # Define the number of pencils Jeanine bought
    jeanine_pencils = 18
    # Calculate the number of pencils Clare bought
    clare_pencils = jeanine_pencils / 2
    # Calculate the number of pencils Jeanine gives to Abby
    abby_pencils = jeanine_pencils / 3
    # Calculate how many pencils Jeanine has left after giving some to Abby
    jeanine_pencils_left = jeanine_pencils - abby_pencils
    # Calculate the difference between the number of pencils Jeanine has left and the number of pencils Clare has
    pencils_difference = jeanine_pencils_left - clare_pencils
    result = pencils_difference
    return result

print(solution())