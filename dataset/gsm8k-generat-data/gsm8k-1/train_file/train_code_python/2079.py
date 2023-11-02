def solution():
    """A hairstylist charges $5 for a normal haircut, $6 for a special haircut, and $8 for a trendy haircut. If he cuts 5 normal haircuts, 3 special haircuts, and 2 trendy haircuts per day, how much money does he earn per week?"""
    normal_haircut_price = 5
    special_haircut_price = 6
    trendy_haircut_price = 8
    normal_haircut_count = 5
    special_haircut_count = 3
    trendy_haircut_count = 2
    per_day_earnings = (normal_haircut_price * normal_haircut_count) + (special_haircut_price * special_haircut_count) + (trendy_haircut_price * trendy_haircut_count)
    weekly_earnings = per_day_earnings * 7
    result = weekly_earnings
    return result

print(solution())