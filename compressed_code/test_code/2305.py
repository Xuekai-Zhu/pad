def solution():
    
    tylenol_dose = 2 * 500 
    hours_per_dose = 4
    total_doses = 12 / hours_per_dose
    total_tylenol_mg = tylenol_dose * total_doses
    total_tylenol_g = total_tylenol_mg / 1000 
    result = total_tylenol_g
    return result

print(solution())