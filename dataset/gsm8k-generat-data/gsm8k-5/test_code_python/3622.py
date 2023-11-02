def solution():
    jeanine_pencils = 18  # Jeanine bought 18 pencils
    clare_pencils = jeanine_pencils / 2  # Clare bought half as many pencils as Jeanine
    jeanine_gave = jeanine_pencils / 3  # Jeanine gave one third of her pencils to Abby
    jeanine_now = jeanine_pencils - jeanine_gave  # Jeanine now has this many pencils
    clare_now = clare_pencils  # Clare didn't give any pencils away
    difference = jeanine_now - clare_now  # Calculate the difference
    result = difference
    return result

print(solution())