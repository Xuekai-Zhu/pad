def solution():
    high_season_rate = 6  # packs per hour
    low_season_rate = 4  # packs per hour
    price_per_pack = 60  # dollars

    high_season_total = high_season_rate * 15 * price_per_pack
    low_season_total = low_season_rate * 15 * price_per_pack

    difference = high_season_total - low_season_total
    result = difference
    return result

print(solution())