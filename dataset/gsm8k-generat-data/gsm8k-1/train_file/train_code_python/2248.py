def solution():
    """At peak season, 6 packs of tuna fish are sold per hour, while in a low season 4 tuna packs are sold per hour. If each tuna pack is sold at $60, How much more money is made in a day during a high season than a low season if the fish are sold for 15 hours?"""
    high_season_sales = 6 * 15
    low_season_sales = 4 * 15
    tuna_pack_price = 60
    high_season_earnings = high_season_sales * tuna_pack_price
    low_season_earnings = low_season_sales * tuna_pack_price
    difference = high_season_earnings - low_season_earnings
    result = difference
    return result

print(solution())