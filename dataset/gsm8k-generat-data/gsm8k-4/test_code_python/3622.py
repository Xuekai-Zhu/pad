def solution():
    """Jeanine bought 18 pencils and Clare bought half as many pencils. If Jeanine gave one third of his pencils to Abby, how many more pencils than Clare does Jeanine have now?"""
    # Define the initial number of pencils Jeanine bought
    jeanine_pencils = 18

    # Define the number of pencils Clare bought
    clare_pencils = jeanine_pencils / 2

    # Calculate the number of pencils Jeanine gave to Abby
    abby_pencils = jeanine_pencils / 3

    # Calculate the number of pencils Jeanine has now
    jeanine_pencils_now = jeanine_pencils - abby_pencils

    # Calculate the difference between Jeanine and Clare's number of pencils
    difference = jeanine_pencils_now - clare_pencils

    # Return the result
    result = difference
    return result

print(solution())