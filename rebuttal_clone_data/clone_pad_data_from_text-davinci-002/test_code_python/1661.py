def solution():
    current_year = 2025
    years_married = 20
    years_dating = 3
    years_before_dating = years_married - years_dating
    result = current_year - years_before_dating - 2
    
    return result

print(solution())