def solution():
    imported_wine = 2400
    domestic_wine = imported_wine / 2
    total_wine = imported_wine + domestic_wine
    
    wine_drunk = total_wine / 3
    
    remaining_wine = total_wine - wine_drunk
    result = remaining_wine
    return result

print(solution())