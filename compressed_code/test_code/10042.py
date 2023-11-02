def solution():
    
    current_chickens = 550
    annual_increase = 150
    years = 9
    total_increase = annual_increase * years
    final_chickens = current_chickens + total_increase
    result = final_chickens
    return result

print(solution())