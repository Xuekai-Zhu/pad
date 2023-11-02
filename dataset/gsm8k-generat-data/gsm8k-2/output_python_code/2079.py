def solution():
    """A hairstylist charges $5 for a normal haircut, $6 for a special haircut, and $8 for a trendy haircut. If he cuts 5 normal haircuts, 3 special haircuts, and 2 trendy haircuts per day, how much money does he earn per week?"""
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