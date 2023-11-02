def solution():
    """Mark has a really bad headache. He takes 2 Tylenol tablets of 500 mg each and he does every 4 hours for 12 hours. How many grams of Tylenol does he end up taking?"""
    tylenol_per_dose = 1000  # 2 tablets x 500 mg each
    doses_per_day = 3  # 12 hours divided by 4 hours per dose
    total_tylenol_mg = tylenol_per_dose * doses_per_day
    total_tylenol_g = total_tylenol_mg / 1000
    result = total_tylenol_g
    return result

print(solution())