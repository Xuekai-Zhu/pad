def solution():
    """Judy uses 10 pencils during her 5 day school week. A 30 pack of pencils costs $4. How much will she spend on pencils over 45 days?"""
    pencils_per_day = 2
    days_in_week = 5
    weeks_in_45_days = 45 / 7
    packs_of_pencils_needed = (pencils_per_day * days_in_week * weeks_in_45_days) / 30
    cost_of_packs_of_pencils = packs_of_pencils_needed * 4
    result = cost_of_packs_of_pencils
    return result

print(solution())