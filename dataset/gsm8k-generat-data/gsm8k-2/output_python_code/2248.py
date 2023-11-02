def solution():
    """At peak season, 6 packs of tuna fish are sold per hour, while in a low season 4 tuna packs are sold per hour. If each tuna pack is sold at $60, How much more money is made in a day during a high season than a low season if the fish are sold for 15 hours?"""
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