def solution():
    """To get clean, Michael takes a bath twice a week and a shower once a week. How many total times does he clean himself in 52 weeks, which is about one year?"""
    baths_per_week = 2
    showers_per_week = 1
    total_cleaning_times = (baths_per_week + showers_per_week) * 52
    result = total_cleaning_times
    return result

print(solution())