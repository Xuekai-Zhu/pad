def solution():
    """Josh has soccer practice on Monday, Wednesday, and Friday from 3:00 p.m. to 5:00 p.m. He has band practice on Tuesday and Thursday from 3:30 p.m. to 5:00 p.m. From Monday to Friday, how many hours does Josh spend on extracurricular activities?"""
    soccer_days = 3
    soccer_hours_per_day = 2
    band_days = 2
    band_hours_per_day = 1.5
    total_hours = (soccer_days * soccer_hours_per_day) + (band_days * band_hours_per_day)
    result = total_hours
    return result

print(solution())