def solution():
    
    imported_wine = 2400
    domestic_wine = imported_wine / 2
    total_wine = imported_wine + domestic_wine
    wine_consumed = total_wine / 3
    wine_remaining = total_wine - wine_consumed
    result = wine_remaining
    return result

print(solution())