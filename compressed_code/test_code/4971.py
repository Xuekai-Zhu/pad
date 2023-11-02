def solution():
    
    total_crayons = 48
    kiley_crayons = total_crayons * 0.25
    remaining_crayons = total_crayons - kiley_crayons
    joe_crayons = remaining_crayons * 0.5
    final_crayons = remaining_crayons - joe_crayons
    result = final_crayons
    return result

print(solution())