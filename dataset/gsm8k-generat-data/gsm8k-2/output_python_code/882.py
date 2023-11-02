def solution():
    """For a project, a builder purchased 7 boxes of bolts with each box containing 11 bolts.
    He purchased 3 boxes of nuts with each box containing 15 nuts.
    He ended up finishing the project 6 days early and with 3 bolts and 6 nuts left over.
    How many bolts and nuts did he use for the project?"""
    bolts_per_box = 11
    nuts_per_box = 15
    total_bolts = 7 * bolts_per_box
    total_nuts = 3 * nuts_per_box
    bolts_left = 3
    nuts_left = 6
    bolts_used = total_bolts - bolts_left
    nuts_used = total_nuts - nuts_left
    result = (bolts_used, nuts_used)
    return result

print(solution())