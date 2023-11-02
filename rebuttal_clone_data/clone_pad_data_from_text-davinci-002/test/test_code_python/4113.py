def solution():
    total_rice = 50
    rice_stored = total_rice * (7/10)
    rice_given = total_rice - rice_stored
    result = rice_stored - rice_given
    
    return result

print(solution())