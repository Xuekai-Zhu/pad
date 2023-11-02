def solution():
    """James takes 2 Tylenol tablets that are 375 mg each, every 6 hours. How many mg does he take a day?"""
    tylenol_dose = 375 * 2
    doses_per_day = 24 / 6
    total_mg_per_day = tylenol_dose * doses_per_day
    result = total_mg_per_day
    return result

print(solution())