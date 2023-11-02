def solution():
    """Akeno spent $2985 to furnish his apartment. Lev spent one-third of that amount on his apartment and Ambrocio spent $177 less than Lev. How many dollars more did Akeno spend than the other 2 people combined?"""
    akeno_spent = 2985
    lev_spent = akeno_spent / 3
    ambrocio_spent = lev_spent - 177
    others_spent = lev_spent + ambrocio_spent
    difference = akeno_spent - others_spent
    result = difference
    return result

print(solution())