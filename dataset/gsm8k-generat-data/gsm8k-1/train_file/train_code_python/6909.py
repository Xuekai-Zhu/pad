def solution():
    """John assembles widgets at a factory. He can make 20 widgets an hour and works for 8 hours a day 5 days a week. How many widgets does he make a week?"""
    widgets_per_hour = 20
    hours_per_day = 8
    days_per_week = 5
    total_widgets = widgets_per_hour * hours_per_day * days_per_week
    result = total_widgets
    return result

print(solution())