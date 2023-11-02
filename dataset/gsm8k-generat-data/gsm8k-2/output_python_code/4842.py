def solution():
    """Josh has soccer practice on Monday, Wednesday, and Friday from 3:00 p.m. to 5:00 p.m. He has band practice on Tuesday and Thursday from 3:30 p.m. to 5:00 p.m. From Monday to Friday, how many hours does Josh spend on extracurricular activities?"""
    soccer_hours_per_day = 2
    band_hours_per_day = 1.5
    soccer_days = 3
    band_days = 2
    total_soccer_hours = soccer_hours_per_day * soccer_days
    total_band_hours = band_hours_per_day * band_days
    total_hours = total_soccer_hours + total_band_hours
    result = total_hours
    return result

print(solution())