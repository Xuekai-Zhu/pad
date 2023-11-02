def solution():
    sam_time = 360  # 6 hours in minutes
    jack_time = 240  # 4 hours in minutes
    tony_time = 480  # 8 hours in minutes
    sam_speed = 1 / 10  # 1 widget every 10 minutes
    jack_speed = 2 / 15  # 2 widgets every 15 minutes
    sam_widgets = sam_time * sam_speed
    jack_widgets = jack_time * jack_speed
    tony_widgets = 68 - sam_widgets - jack_widgets
    tony_speed = tony_widgets / tony_time
    tony_time_per_widget = 1 / tony_speed
    result = tony_time_per_widget
    return result

print(solution())