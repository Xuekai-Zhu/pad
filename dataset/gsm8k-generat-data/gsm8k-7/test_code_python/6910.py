def solution():
    widgets_per_hour = 20
    hours_per_day = 8
    days_per_week = 5

    # Calculate the total number of hours worked in a week
    total_hours = hours_per_day * days_per_week

    # Calculate the total number of widgets John can make in a week
    total_widgets = widgets_per_hour * total_hours
    result = total_widgets
    return result

print(solution())