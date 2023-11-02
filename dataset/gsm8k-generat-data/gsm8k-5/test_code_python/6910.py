def solution():
    widgets_per_hour = 20  # John can make 20 widgets per hour
    hours_per_day = 8  # John works 8 hours per day
    days_per_week = 5  # John works 5 days per week

    # Calculate the total number of widgets John makes in a week
    total_widgets = widgets_per_hour * hours_per_day * days_per_week
    result = total_widgets
    return result

print(solution())