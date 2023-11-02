def solution():
    
    initial_biscuits = 32
    father_gift = 13
    mother_gift = 15
    brother_eaten = 20
    total_biscuits = initial_biscuits + father_gift + mother_gift - brother_eaten
    result = total_biscuits
    return result

print(solution())