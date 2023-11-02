def solution():
    num_horses = 80
    daily_fert_production = num_horses * 5  # 5 gallons of fertilizer per horse per day
    total_fert_needed = 20 * 400  # 20 acres of farmland each needing 400 gallons of fertilizer
    days_to_spread_fert = total_fert_needed / (4 * daily_fert_production)  # 4 acres spread per day per horse
        
    result = days_to_spread_fert
    return result

print(solution())