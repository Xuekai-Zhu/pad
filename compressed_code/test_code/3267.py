def solution():
    
    current_height = 50
    growth_rate = 0.5   
    years = 12 - 8     
    total_growth = growth_rate * years
    final_height = current_height + (total_growth * 12)  
    result = final_height
    return result

print(solution())