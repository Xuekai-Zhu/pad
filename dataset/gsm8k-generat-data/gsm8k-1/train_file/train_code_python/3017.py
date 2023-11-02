def solution():
    """Kara has to drink 4 ounces of water every time she takes her medication. Her medication instructions are to take one tablet three times a day. She followed the instructions for one week, but in the second week, she forgot twice on one day. How many ounces of water did she drink with her medication over those two weeks?"""
    water_per_med = 4
    meds_per_day = 3
    days_week1 = 7
    days_week2 = 6  # subtracting the two days she forgot to take her medication
    total_meds = (meds_per_day * days_week1) + (meds_per_day * (days_week2 - 1))  # subtracting 1 for the day she forgot twice
    total_water = total_meds * water_per_med
    result = total_water
    return result

print(solution())