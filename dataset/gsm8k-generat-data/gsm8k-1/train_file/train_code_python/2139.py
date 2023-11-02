def solution():
    """James takes 2 Tylenol tablets that are 375 mg each, every 6 hours. How many mg does he take a day?"""
    tablets_per_dose = 2
    mg_per_tablet = 375
    doses_per_day = 4
    total_mg_per_day = tablets_per_dose * mg_per_tablet * doses_per_day
    result = total_mg_per_day
    return result

print(solution())