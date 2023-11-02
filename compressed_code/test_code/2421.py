def solution():
    
    old_rent = 2 * 750  
    new_rent = 2800 / 2  
    savings_per_month = old_rent - new_rent
    savings_per_year = savings_per_month * 12
    result = savings_per_year
    return result

print(solution())