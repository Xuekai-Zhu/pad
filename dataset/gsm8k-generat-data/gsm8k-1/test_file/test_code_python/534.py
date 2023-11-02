def solution():
    """Emma can make and upload 72 vlogs per month. But she was only able to make 18 vlogs for the first week, 21 vlogs for the second week, and 15 vlogs for the third week. How many vlogs should she do to complete the 72 vlogs per month?"""
    vlogs_per_month = 72
    vlogs_first_week = 18
    vlogs_second_week = 21
    vlogs_third_week = 15
    vlogs_left = vlogs_per_month - (vlogs_first_week + vlogs_second_week + vlogs_third_week)
    result = vlogs_left
    return result

print(solution())