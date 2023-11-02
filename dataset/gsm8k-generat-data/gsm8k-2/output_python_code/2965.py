def solution():
    """Mark has a really bad headache. He takes 2 Tylenol tablets of 500 mg each and he does every 4 hours for 12 hours. How many grams of Tylenol does he end up taking?"""
    tylenol_dose = 2 * 500 # in milligrams
    hours_per_dose = 4
    total_doses = 12 / hours_per_dose
    total_tylenol_mg = tylenol_dose * total_doses
    total_tylenol_g = total_tylenol_mg / 1000 # convert to grams
    result = total_tylenol_g
    return result

print(solution())