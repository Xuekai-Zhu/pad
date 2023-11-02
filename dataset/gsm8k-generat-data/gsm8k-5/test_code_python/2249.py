def solution():
    tuna_packs_per_hour_high_season = 6
    tuna_packs_per_hour_low_season = 4
    tuna_pack_price = 60
    hours_per_day = 15

    # Calculate the total revenue in a day during the high season
    revenue_high_season = tuna_packs_per_hour_high_season * tuna_pack_price * hours_per_day

    # Calculate the total revenue in a day during the low season
    revenue_low_season = tuna_packs_per_hour_low_season * tuna_pack_price * hours_per_day

    # Calculate the difference in revenue between the high season and low season
    revenue_difference = revenue_high_season - revenue_low_season
    result = revenue_difference
    return result

print(solution())