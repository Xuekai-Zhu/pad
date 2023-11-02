def solution():
    
    total_food = 0
    
    
    for i in range(0, 14):
        total_food += (1/4) * 3
    
    
    for i in range(0, 14):
        total_food += (1/2) * 2
    
    
    total_food += 0.5
    
    result = total_food
    return result

print(solution())