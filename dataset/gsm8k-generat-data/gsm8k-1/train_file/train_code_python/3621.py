def solution():
    """Jeanine bought 18 pencils and Clare bought half as many pencils. If Jeanine gave one third of his pencils to Abby, how many more pencils than Clare does Jeanine have now?"""
    jeanine_pencils = 18
    clare_pencils = jeanine_pencils / 2
    abby_pencils = jeanine_pencils / 3
    remaining_pencils = jeanine_pencils - abby_pencils
    difference = remaining_pencils - clare_pencils
    result = difference
    return result

print(solution())