def solution():
    
    high_season_packs_per_hour = 6
    low_season_packs_per_hour = 4
    price_per_pack = 60
    hours_per_day = 15

    high_season_total_packs = high_season_packs_per_hour * hours_per_day
    low_season_total_packs = low_season_packs_per_hour * hours_per_day

    high_season_earnings = high_season_total_packs * price_per_pack
    low_season_earnings = low_season_total_packs * price_per_pack

    diff = high_season_earnings - low_season_earnings

    result = diff
    return result

print(solution())