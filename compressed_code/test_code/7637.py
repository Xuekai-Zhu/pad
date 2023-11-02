def solution():
    
    pounds_of_eggs = 6
    weight_of_one_egg = 1/16
    number_of_eggs = pounds_of_eggs / weight_of_one_egg
    number_of_dozen = number_of_eggs / 12
    result = number_of_dozen
    return result

print(solution())