def solution():
    
    basswood_figurines = 3
    butternut_figurines = 4
    aspen_figurines = 2 * basswood_figurines
    
    total_basswood_figurines = basswood_figurines * 15
    total_butternut_figurines = butternut_figurines * 20
    total_aspen_figurines = aspen_figurines * 20
    
    total_figurines = total_basswood_figurines + total_butternut_figurines + total_aspen_figurines
    
    result = total_figurines
    return result

print(solution())