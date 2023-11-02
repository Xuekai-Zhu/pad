def solution():
    tylenol_dose = 500  # in mg
    num_doses = 3  # every 4 hours for 12 hours
    total_tylenol_mg = tylenol_dose * 2 * num_doses  # 2 tablets per dose
    total_tylenol_grams = total_tylenol_mg / 1000
    result = total_tylenol_grams
    return result

print(solution())