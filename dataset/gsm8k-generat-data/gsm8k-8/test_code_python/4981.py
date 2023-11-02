def solution():
    total_spent = 2985
    lev_spent = total_spent / 3
    ambrocio_spent = lev_spent - 177
    combined_spent = lev_spent + ambrocio_spent
    difference = total_spent - combined_spent
    result = difference
    return result

print(solution())