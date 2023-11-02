def solution():
    
    total_crayons = 4 * 8
    total_crayons -= 5  
    remaining_crayons = 15  
    lea_crayons = total_crayons - remaining_crayons
    mae_crayons = 5  
    difference = lea_crayons - mae_crayons
    result = difference
    return result

print(solution())