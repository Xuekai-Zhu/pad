def solution():
    """John likes to have a glass of water with breakfast, lunch and dinner. Finally, he has one before he goes to bed as well. John does this every weekday, but on the weekends he likes to relax and have a soda with dinner instead. How many glasses of water does John drink in a week?"""
    water_per_weekday = 4
    water_per_weekend = 3
    days_per_week = 7
    total_water = (water_per_weekday * 5) + (water_per_weekend * 2)
    result = total_water
    return result

print(solution())