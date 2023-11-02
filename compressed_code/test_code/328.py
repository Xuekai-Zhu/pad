def solution():
    
    original_amoebae = 1
    final_amoebae = 16
    division_time = 2
    num_divisions = 0
    while original_amoebae < final_amoebae:
        original_amoebae *= 2
        num_divisions += 1
    
    result = num_divisions * division_time
    return result

print(solution())