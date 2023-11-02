def solution():
    sam_per_hour = 60 / 10
    jack_per_hour = 60 / 15 * 2
    total_per_hour = sam_per_hour + jack_per_hour
    hours_worked = 6 + 4
    widgets_made = 68
    minutes_per_widget = hours_worked * 60 / widgets_made
    result = minutes_per_widget
    return result

print(solution())