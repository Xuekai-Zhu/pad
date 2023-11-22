def solution():
    
    total_kids = 32
    dairy_allergic = 9
    peanut_allergic = 6
    both_allergic = 3
    non_allergic = total_kids - dairy_allergic - peanut_allergic - both_allergic
    result = non_allergic
    return result

print(solution())