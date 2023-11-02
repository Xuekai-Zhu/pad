def solution():
    
    akeno_spent = 2985
    lev_spent = akeno_spent / 3
    ambrocio_spent = lev_spent - 177
    total_spent = lev_spent + ambrocio_spent
    difference = akeno_spent - total_spent
    result = difference
    return result

print(solution())