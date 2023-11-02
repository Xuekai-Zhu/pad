def solution():
    
    akeno_spent = 2985
    lev_spent = akeno_spent / 3
    ambrocio_spent = lev_spent - 177
    others_spent = lev_spent + ambrocio_spent
    difference = akeno_spent - others_spent
    result = difference
    return result

print(solution())