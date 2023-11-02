def solution():
    normal_haircut = 5
    special_haircut = 6
    trendy_haircut = 8
    haircuts_per_day = normal_haircut + special_haircut + trendy_haircut
    price_normal_haircut = 5
    price_special_haircut = 6
    price_trendy_haircut = 8
    daily_earnings = (normal_haircut * price_normal_haircut) + (special_haircut * price_special_haircut) + (trendy_haircut * price_trendy_haircut)
    weekly_earnings = daily_earnings * 7
    result = weekly_earnings
    return result

print(solution())