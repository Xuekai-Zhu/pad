def solution():
    
    high_season_sales = 6 * 15
    low_season_sales = 4 * 15
    tuna_pack_price = 60
    high_season_earnings = high_season_sales * tuna_pack_price
    low_season_earnings = low_season_sales * tuna_pack_price
    difference = high_season_earnings - low_season_earnings
    result = difference
    return result

print(solution())