def solution():
    
    normal_price = 5
    special_price = 6
    trendy_price = 8
    normal_per_day = 5
    special_per_day = 3
    trendy_per_day = 2
    days_per_week = 7
    total_normal = normal_per_day * days_per_week
    total_special = special_per_day * days_per_week
    total_trendy = trendy_per_day * days_per_week
    total_price = (total_normal * normal_price) + (total_special * special_price) + (total_trendy * trendy_price)
    result = total_price
    return result

print(solution())