def solution():
    
    tylenol_per_dose = 1000  
    doses_per_day = 3  
    total_tylenol_mg = tylenol_per_dose * doses_per_day
    total_tylenol_g = total_tylenol_mg / 1000
    result = total_tylenol_g
    return result

print(solution())