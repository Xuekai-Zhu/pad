def solution():
    
    initial_biscuits = 32
    father_biscuits = 13
    mother_biscuits = 15
    brother_biscuits = 20
    total_biscuits = initial_biscuits + father_biscuits + mother_biscuits - brother_biscuits
    result = total_biscuits
    return result

print(solution())