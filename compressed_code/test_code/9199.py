def solution():
    
    red_snapper_count = 8
    tuna_count = 14
    red_snapper_price = 3
    tuna_price = 2
    total_red_snapper_earnings = red_snapper_count * red_snapper_price
    total_tuna_earnings = tuna_count * tuna_price
    daily_earnings = total_red_snapper_earnings + total_tuna_earnings
    result = daily_earnings
    return result

print(solution())