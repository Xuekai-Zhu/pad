def solution():
    
    current_chickens = 550
    annual_increase = 150
    years = 9
    total_chickens = current_chickens + (annual_increase * years)
    result = total_chickens
    return result

print(solution())