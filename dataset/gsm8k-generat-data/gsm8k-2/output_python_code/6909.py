def solution():
    """John assembles widgets at a factory. He can make 20 widgets an hour and works for 8 hours a day 5 days a week. How many widgets does he make a week?"""
    widgets_per_hour = 20
    hours_per_day = 8
    days_per_week = 5
    widgets_per_week = widgets_per_hour * hours_per_day * days_per_week
    result = widgets_per_week
    return result

print(solution())