def solution():
    
    initial_weight = 5
    perfume_weight = 5 * 1.2 / 16  
    chocolate_weight = 4
    soap_weight = 2 * 5 / 16  
    jam_weight = 2 * 8 / 16  
    return_weight = initial_weight + perfume_weight + chocolate_weight + soap_weight + jam_weight
    result = return_weight
    return result

print(solution())