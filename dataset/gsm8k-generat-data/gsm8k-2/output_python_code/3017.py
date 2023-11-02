def solution():
    """Kara has to drink 4 ounces of water every time she takes her medication. Her medication instructions are to take one tablet three times a day. She followed the instructions for one week, but in the second week, she forgot twice on one day. How many ounces of water did she drink with her medication over those two weeks?"""
    water_per_medication = 4
    total_medication_per_day = 3
    total_days_first_week = 7
    total_days_second_week = 7
    total_water_first_week = water_per_medication * total_medication_per_day * total_days_first_week
    total_water_second_week = (water_per_medication * total_medication_per_day * (total_days_second_week - 1)) + (water_per_medication * 2)
    total_water = total_water_first_week + total_water_second_week
    result = total_water
    return result

print(solution())