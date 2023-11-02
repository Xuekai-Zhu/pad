def solution():
    """Brittany uses 1/4 ounce of shampoo to wash her hair every other day. She buys shampoo in 14-ounce bottles. How many bottles does she need to get her through a leap year?"""
    shampoo_used_per_day = 1/4
    days_in_leap_year = 366
    days_without_washing_hair = days_in_leap_year // 2
    total_shampoo_used = shampoo_used_per_day * days_without_washing_hair
    bottles_needed = total_shampoo_used / 14
    result = math.ceil(bottles_needed)
    return result

print(solution())