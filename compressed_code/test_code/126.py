def solution():
    
    current_grape_usage = 90
    increased_percentage = 0.2
    new_grape_usage = current_grape_usage * (1 + increased_percentage)
    grapes_per_year = new_grape_usage * 2
    result = grapes_per_year
    return result

print(solution())